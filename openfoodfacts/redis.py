import datetime
from typing import Any, Iterator, Optional, Union, cast

from pydantic import BaseModel, Json
from redis import Redis

from openfoodfacts.utils import get_logger

logger = get_logger(__name__)


def get_redis_client(**kwargs) -> Redis:
    return Redis(
        decode_responses=True,
        **kwargs,
    )


class RedisUpdate(BaseModel):
    """A class representing a product update from a Redis Stream."""

    stream: str
    timestamp: datetime.datetime
    code: str
    flavor: str
    user_id: str
    action: str
    comment: str
    diffs: Optional[Json[Any]] = None


def get_processed_since(
    redis_client: Redis,
    start_timestamp: Union[int, datetime.datetime],
    redis_stream_name: str = "product_updates_off",
    batch_size: int = 100,
) -> Iterator[RedisUpdate]:
    """Fetches all the updates that have been published since the given
    timestamp.

    :param redis_client: the Redis client
    :param start_timestamp: the timestamp to start from, in milliseconds, or a
        datetime
    :param redis_stream_name: the name of the Redis stream to read from
    :param batch_size: the size of the batch to fetch, defaults to 100
    :yield: a RedisUpdate instance for each update
    """
    if isinstance(start_timestamp, datetime.datetime):
        start_timestamp = int(start_timestamp.timestamp() * 1000)

    # We start from the given timestamp
    min_id = f"{start_timestamp}-0"

    while True:
        logger.debug(
            "Fetching batch from Redis, stream %s, min_id %s, count %d",
            redis_stream_name,
            min_id,
            batch_size,
        )
        batch = redis_client.xrange(redis_stream_name, min=min_id, count=batch_size)
        if not batch:
            # We reached the end of the stream
            break

        batch = cast(list[tuple[str, dict]], batch)
        # We update the min_id to the last ID of the batch
        min_id = f"({batch[-1][0]}"
        for timestamp_id, item in batch:
            # Get the timestamp from the ID
            timestamp = int(timestamp_id.split("-")[0])
            yield RedisUpdate(
                timestamp=timestamp,  # type: ignore
                stream=redis_stream_name,
                code=item["code"],
                flavor=item["flavor"],
                user_id=item["user_id"],
                action=item["action"],
                comment=item["comment"],
                diffs=item.get("diffs"),
            )


def get_new_updates(
    redis_client: Redis,
    stream_name: str = "product_updates_off",
    batch_size: int = 100,
) -> Iterator[RedisUpdate]:
    """Reads new updates from a Redis Stream, starting from the moment this
    function is called.

    The function will block until new updates are available.

    :param redis_client: the Redis client
    :param stream_name: the name of the Redis stream to read from
    :param batch_size: the size of the batch to fetch, defaults to 100
    :yield: a RedisUpdate instance for each update
    """
    yield from get_new_updates_multistream(
        redis_client,
        [stream_name],
        batch_size=batch_size,
    )


def get_new_updates_multistream(
    redis_client: Redis,
    stream_names: list[str],
    batch_size: int = 100,
) -> Iterator[RedisUpdate]:
    """Reads new updates from Redis Stream, starting from the moment this
    function is called.

    The function will block until new updates are available.

    :param redis_client: the Redis client
    :param stream_names: the names of the Redis streams to read from
    :param batch_size: the size of the batch to fetch, defaults to 100.
    :yield: a RedisUpdate instance for each update
    """
    # We start from the last ID
    min_ids: dict[Union[bytes, str, memoryview], Union[int, bytes, str, memoryview]] = {
        stream_name: "$" for stream_name in stream_names
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
            min_id = batch[-1][0]
            min_ids[stream_name] = min_id
            for timestamp_id, item in batch:
                # Get the timestamp from the ID
                timestamp = int(timestamp_id.split("-")[0])
                yield RedisUpdate(
                    timestamp=timestamp,  # type: ignore
                    stream=stream_name,
                    code=item["code"],
                    flavor=item["flavor"],
                    user_id=item["user_id"],
                    action=item["action"],
                    comment=item["comment"],
                    diffs=item.get("diffs"),
                )
