import datetime
import logging
from typing import Any, Iterator, cast

from pydantic import BaseModel, Json
from redis import Redis

logger = logging.getLogger(__name__)


def get_redis_client(**kwargs) -> Redis:
    return Redis(
        decode_responses=True,
        **kwargs,
    )


class ProductUpdateEvent(BaseModel):
    """A class representing a product update from a Redis Stream."""

    # The Redis ID of the event
    id: str
    # The name of the Redis stream where the update was published
    # This will always be "product_updates"
    stream: str
    # The timestamp of the event
    timestamp: datetime.datetime
    # The code of the product
    code: str
    # The flavor of the product (off, obf, opff, off_pro)
    flavor: str
    # The user ID of the user who performed the action
    user_id: str
    # The action performed by the user (either updated or deleted)
    action: str
    # A comment provided by the user
    comment: str
    # the type of the product (food, product, petfood, beauty)
    product_type: str
    # A JSON object representing the differences between the old and new
    # product data
    diffs: Json[Any] | None = None

    def is_image_upload(self) -> bool:
        """Returns True if the update is an image upload."""
        return bool(
            self.diffs is not None
            and "uploaded_images" in self.diffs
            and "add" in self.diffs["uploaded_images"]
        )

    def is_product_type_change(self) -> bool:
        """Returns True if the update contains a product type change (example:
        switch from `food` to `beauty`)."""
        return bool(
            self.diffs is not None
            and "fields" in self.diffs
            and "change" in self.diffs["fields"]
            and "product_type" in self.diffs["fields"]["change"]
        )

    def is_field_updated(self, field_name: str) -> bool:
        """Returns True if the update contains a change in the specified
        field."""
        return (
            self.diffs is not None
            and "fields" in self.diffs
            and "change" in self.diffs["fields"]
            and field_name in self.diffs["fields"]["change"]
        )

    def is_field_added(self, field_name: str) -> bool:
        """Returns True if the update contains a change in the specified
        field."""
        return (
            self.diffs is not None
            and "fields" in self.diffs
            and "add" in self.diffs["fields"]
            and field_name in self.diffs["fields"]["add"]
        )

    def is_field_added_or_updated(self, field_name: str) -> bool:
        """Returns True if the update contains a change in the specified
        field."""
        return self.is_field_updated(field_name) or self.is_field_added(field_name)

    def is_image_deletion(self) -> bool:
        """Returns True if the event is an image deletion."""
        return (
            self.diffs is not None
            and "uploaded_images" in self.diffs
            and "delete" in self.diffs["uploaded_images"]
        )


class OCRReadyEvent(BaseModel):
    """A class representing an OCR ready event from a Redis Stream.

    This event is published when the OCR processing (done by Google Cloud
    Vision) of an image is complete.

    The OCR result (JSON file) is available at the URL provided in the
    `json_url` field.
    """

    # The Redis ID of the event
    id: str
    # The name of the Redis stream where the event was published
    # This will always be "ocr_ready"
    stream: str
    # The timestamp of the event
    timestamp: datetime.datetime
    # The code of the product
    code: str
    # the type of the product (food, product, petfood, beauty)
    product_type: str
    # The ID of the image (ex: "1")
    image_id: str
    # The URL of the OCR result (JSON file)
    json_url: str


def get_processed_since(
    redis_client: Redis,
    min_id: str | datetime.datetime,
    product_updates_stream_name: str = "product_updates",
    ocr_ready_stream_name: str = "ocr_ready",
    batch_size: int = 100,
) -> Iterator[ProductUpdateEvent | OCRReadyEvent]:
    """Fetches all events (product update or ocr ready events) that have been
    published since the given timestamp.

    :param redis_client: the Redis client
    :param min_id: the minimum ID to start from, or a datetime object
    :param product_updates_stream_name: the name of the Redis stream for
        product updates, defaults to "product_updates"
    :param ocr_ready_stream_name: the name of the Redis stream for OCR ready
        events, defaults to "ocr_ready"
    :param batch_size: the size of the batch to fetch, defaults to 100
    :yield: a ProductUpdateEvent or OCRReadyEvent instance for each update
    """
    if isinstance(min_id, datetime.datetime):
        min_id = f"{int(min_id.timestamp() * 1000)}-0"

    for stream_name in (
        product_updates_stream_name,
        ocr_ready_stream_name,
    ):
        while True:
            logger.debug(
                "Fetching batch from Redis, stream %s, min_id %s, count %d",
                stream_name,
                min_id,
                batch_size,
            )
            batch = redis_client.xrange(stream_name, min=min_id, count=batch_size)
            if not batch:
                # We reached the end of the stream
                break

            batch = cast(list[tuple[str, dict]], batch)
            # We update the min_id to the last ID of the batch
            min_id = f"({batch[-1][0]}"
            for timestamp_id, item in batch:
                # Get the timestamp from the ID
                timestamp = int(timestamp_id.split("-")[0])

                if stream_name == ocr_ready_stream_name:
                    yield OCRReadyEvent(
                        id=timestamp_id,
                        timestamp=timestamp,  # type: ignore
                        stream=stream_name,
                        code=item["code"],
                        product_type=item["product_type"],
                        image_id=item["image_id"],
                        json_url=item["json_url"],
                    )
                else:
                    yield ProductUpdateEvent(
                        id=timestamp_id,
                        timestamp=timestamp,  # type: ignore
                        stream=stream_name,
                        code=item["code"],
                        flavor=item["flavor"],
                        user_id=item["user_id"],
                        action=item["action"],
                        comment=item["comment"],
                        product_type=item["product_type"],
                        diffs=item.get("diffs"),
                    )


def get_new_updates_multistream(
    redis_client: Redis,
    product_updates_stream_name: str = "product_updates",
    ocr_ready_stream_name: str = "ocr_ready",
    min_id: str | datetime.datetime | None = "$",
    batch_size: int = 100,
) -> Iterator[ProductUpdateEvent | OCRReadyEvent]:
    """Reads new updates from Redis Stream, starting from the moment this
    function is called.

    The function will block until new updates are available.

    :param redis_client: the Redis client.
    :param product_updates_stream_name: the name of the Redis stream for
        product updates, defaults to "product_updates".
    :param ocr_ready_stream_name: the name of the Redis stream for OCR ready
        events, defaults to "ocr_ready".
    :param min_id: the minimum ID to start from, defaults to "$".
    :param batch_size: the size of the batch to fetch, defaults to 100.
    :yield: a ProductUpdateEvent or OCRReadyEvent instance for each update.
    """
    if min_id is None:
        min_id = "$"
    elif isinstance(min_id, datetime.datetime):
        min_id = f"{int(min_id.timestamp() * 1000)}-0"

    stream_names = [product_updates_stream_name, ocr_ready_stream_name]
    # We start from the last ID
    min_ids: dict[bytes | str | memoryview, int | bytes | str | memoryview] = {
        stream_name: min_id for stream_name in stream_names
    }
    while True:
        logger.debug(
            "Listening to new updates from streams %s (ID: %s)", stream_names, min_ids
        )
        # We use block=0 to wait indefinitely for new updates
        response = redis_client.xread(streams=min_ids, block=0, count=batch_size)
        response = cast(list[tuple[str, list[tuple[str, dict]]]], response)
        # The response is a list of tuples (stream_name, batch)

        for stream_name, batch in response:
            # We update the min_id to the last ID of the batch
            new_min_id = batch[-1][0]
            min_ids[stream_name] = new_min_id
            for timestamp_id, item in batch:
                # Get the timestamp from the ID
                timestamp = int(timestamp_id.split("-")[0])

                if stream_name == ocr_ready_stream_name:
                    yield OCRReadyEvent(
                        id=timestamp_id,
                        stream=stream_name,
                        timestamp=timestamp,  # type: ignore
                        code=item["code"],
                        product_type=item["product_type"],
                        image_id=item["image_id"],
                        json_url=item["json_url"],
                    )
                else:
                    yield ProductUpdateEvent(
                        id=timestamp_id,
                        stream=stream_name,
                        timestamp=timestamp,  # type: ignore
                        code=item["code"],
                        flavor=item["flavor"],
                        user_id=item["user_id"],
                        action=item["action"],
                        comment=item["comment"],
                        product_type=item["product_type"],
                        diffs=item.get("diffs"),
                    )


class UpdateListener:
    """A class representing a daemon that listens to events from a Redis
    stream and processes them.

    The class is meant to be subclassed to implement the processing logic.
    Subclasses can implement the `process_redis_update` and
    `process_ocr_ready` methods.
    """

    def __init__(
        self,
        redis_client: Redis,
        redis_latest_id_key: str,
        product_updates_stream_name: str = "product_updates",
        ocr_ready_stream_name: str = "ocr_ready",
    ):
        self.redis_client = redis_client
        self.product_updates_stream_name = product_updates_stream_name
        self.ocr_ready_stream_name = ocr_ready_stream_name
        self.redis_latest_id_key = redis_latest_id_key

    def run(self):
        """Run the update import daemon.

        This daemon listens to the Redis stream containing information about
        product updates or OCR ready events, and processes them as they
        arrive.
        """
        logger.info("Starting update listener daemon")

        logger.info("Redis client: %s", self.redis_client)
        logger.info("Pinging client...")
        self.redis_client.ping()
        logger.info("Connection successful")

        latest_id = self.redis_client.get(self.redis_latest_id_key)

        if latest_id:
            logger.info(
                "Latest ID processed: %s (datetime: %s)",
                latest_id,
                datetime.datetime.fromtimestamp(int(latest_id.split("-")[0]) / 1000),
            )
        else:
            logger.info("No latest ID found")

        for event in get_new_updates_multistream(
            self.redis_client,
            min_id=latest_id,
        ):
            try:
                if isinstance(event, OCRReadyEvent):
                    self.process_ocr_ready(event)
                else:
                    self.process_redis_update(event)
            except Exception as e:
                logger.exception(e)
            self.redis_client.set(self.redis_latest_id_key, event.id)

    def process_updates_since(
        self, since: datetime.datetime, to: datetime.datetime | None = None
    ):
        """Process all the updates since the given timestamp.

        :param client: the Redis client
        :param since: the timestamp to start from
        :param to: the timestamp to stop, defaults to None (process all
            updates)
        """
        logger.info("Redis client: %s", self.redis_client)
        logger.info("Pinging client...")
        self.redis_client.ping()

        processed = 0
        for event in get_processed_since(
            self.redis_client,
            min_id=since,
        ):
            if to is not None and event.timestamp > to:
                break
            if isinstance(event, OCRReadyEvent):
                self.process_ocr_ready(event)
            else:
                self.process_redis_update(event)

            processed += 1

        logger.info("Processed %d events", processed)

    def process_redis_update(self, event: ProductUpdateEvent):
        pass

    def process_ocr_ready(self, event: OCRReadyEvent):
        pass
