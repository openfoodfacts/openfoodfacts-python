import datetime
import json
from typing import Optional, cast

import pytest
from redis import Redis

from openfoodfacts.redis import (
    ProductUpdateEvent,
    get_new_updates_multistream,
    get_processed_since,
)


class TestRedisUpdate:
    @pytest.mark.parametrize(
        "diffs, expected",
        [
            ({"uploaded_images": {"add": ["2"]}}, True),
            ({"fields": {"change": {"product_type": "food"}}}, False),
            (None, False),
        ],
    )
    def test_is_image_upload(self, diffs, expected):
        update = ProductUpdateEvent(
            id="1629878400000-0",
            stream="product_updates",
            timestamp=1629878400000,
            code="1",
            flavor="off",
            user_id="user1",
            action="updated",
            comment="comment",
            product_type="food",
            diffs=json.dumps(diffs) if diffs is not None else None,
        )
        assert update.is_image_upload() is expected

    @pytest.mark.parametrize(
        "diffs, expected",
        [
            ({"fields": {"change": ["product_type"]}}, True),
            ({"fields": {"change": ["countries", "product_type"]}}, True),
            ({"fields": {"change": ["countries"]}}, False),
            (None, False),
        ],
    )
    def test_is_product_type_change(self, diffs, expected):
        update = ProductUpdateEvent(
            id="1629878400000-0",
            stream="product_updates",
            timestamp=1629878400000,
            code="1",
            flavor="off",
            user_id="user1",
            action="updated",
            comment="comment",
            product_type="food",
            diffs=json.dumps(diffs) if diffs is not None else None,
        )
        assert update.is_product_type_change() is expected

    @pytest.mark.parametrize(
        "diffs, field_name, expected",
        [
            (
                {"fields": {"change": ["product_name", "quantity"]}},
                "product_name",
                True,
            ),
            ({"fields": {"change": ["product_name", "quantity"]}}, "countries", False),
            ({"uploaded_images": {"add": ["4"]}}, "countries", False),
            ({}, "countries", False),
            (None, "product_name", False),
        ],
    )
    def test_is_field_updated(self, diffs, field_name, expected):
        update = ProductUpdateEvent(
            id="1629878400000-0",
            stream="product_updates",
            timestamp=1629878400000,
            code="1",
            flavor="off",
            user_id="user1",
            action="updated",
            comment="comment",
            product_type="food",
            diffs=json.dumps(diffs) if diffs is not None else None,
        )
        assert update.is_field_updated(field_name) is expected

    @pytest.mark.parametrize(
        "diffs, field_name, expected",
        [
            (
                {"fields": {"add": ["product_name", "quantity"]}},
                "product_name",
                True,
            ),
            ({"fields": {"add": ["product_name"]}}, "countries", False),
            ({"uploaded_images": {"add": ["4"]}}, "countries", False),
            ({}, "countries", False),
            (None, "product_name", False),
        ],
    )
    def test_is_field_added(self, diffs, field_name, expected):
        update = ProductUpdateEvent(
            id="1629878400000-0",
            stream="product_updates",
            timestamp=1629878400000,
            code="1",
            flavor="off",
            user_id="user1",
            action="updated",
            comment="comment",
            product_type="food",
            diffs=json.dumps(diffs) if diffs is not None else None,
        )
        assert update.is_field_added(field_name) is expected

    @pytest.mark.parametrize(
        "diffs, field_name, expected",
        [
            (
                {"fields": {"change": ["product_name", "quantity"]}},
                "product_name",
                True,
            ),
            ({"fields": {"change": ["product_name", "quantity"]}}, "countries", False),
            (
                {"fields": {"add": ["product_name", "quantity"]}},
                "product_name",
                True,
            ),
            ({"fields": {"add": ["product_name"]}}, "countries", False),
            ({"uploaded_images": {"add": ["4"]}}, "countries", False),
            ({}, "countries", False),
            (None, "product_name", False),
        ],
    )
    def test_is_field_added_or_updated(self, diffs, field_name, expected):
        update = ProductUpdateEvent(
            id="1629878400000-0",
            stream="product_updates",
            timestamp=1629878400000,
            code="1",
            flavor="off",
            user_id="user1",
            action="updated",
            comment="comment",
            product_type="food",
            diffs=json.dumps(diffs) if diffs is not None else None,
        )
        assert update.is_field_added_or_updated(field_name) is expected

    @pytest.mark.parametrize(
        "diffs, expected",
        [
            (
                {
                    "selected_images": {"delete": ["front_de"]},
                    "uploaded_images": {"delete": ["1"]},
                },
                True,
            ),
            ({"fields": {"add": ["product_name"]}}, False),
            ({"uploaded_images": {"add": ["4"]}}, False),
            ({}, False),
            (None, False),
        ],
    )
    def test_is_image_deletion(self, diffs, expected):
        update = ProductUpdateEvent(
            id="1629878400000-0",
            stream="product_updates",
            timestamp=1629878400000,
            code="1",
            flavor="off",
            user_id="user1",
            action="updated",
            comment="comment",
            product_type="food",
            diffs=json.dumps(diffs),
        )
        assert update.is_image_deletion() is expected


class RedisXrangeClient:
    def __init__(self, xrange_return_values: list):
        self.xrange_return_values = xrange_return_values
        self.call_count = 0

    def xrange(
        self, name: str, min: str = "-", max: str = "+", count: Optional[int] = None
    ):
        assert name in ("product_updates", "ocr_ready")
        assert max == "+"
        assert count == 100
        if self.call_count >= len(self.xrange_return_values):
            return []
        self.call_count += 1
        return self.xrange_return_values[self.call_count - 1]


def test_get_processed_since():
    stream_name = "product_updates"
    base_values = {
        "flavor": "off",
        "user_id": "user1",
        "action": "updated",
        "comment": "comment",
        "product_type": "food",
    }
    return_values = [
        [
            ("1629878400000-0", {"code": "2", **base_values}),
            ("1629878400001-0", {"code": "3", **base_values}),
        ]
    ]
    redis_client = cast(Redis, RedisXrangeClient(return_values))
    # Wed Aug 25 08:00:00 2021 UTC
    start_timestamp_ms = 1629878400000  # Example start timestamp
    # Call the function and iterate over the results
    results = list(
        get_processed_since(
            redis_client,
            min_id=start_timestamp_ms,
        )
    )

    # Assertions
    assert len(results) == 2
    assert results[0] == ProductUpdateEvent(
        id="1629878400000-0",
        stream=stream_name,
        timestamp=1629878400000,
        code="2",
        **base_values,
    )
    assert results[1] == ProductUpdateEvent(
        id="1629878400001-0",
        stream=stream_name,
        timestamp=1629878400001,
        code="3",
        **base_values,
    )


class RedisXreadClient:
    def __init__(self, xread_return_values: list):
        self.xread_return_values = xread_return_values
        self.call_count = 0

    def xread(self, streams: dict, block: int, count: Optional[int] = None):
        assert set(streams.keys()) == {"product_updates", "ocr_ready"}
        assert block == 0
        assert count == 100
        if self.call_count >= len(self.xread_return_values):
            raise ValueError("No more values")
        self.call_count += 1
        return self.xread_return_values[self.call_count - 1]


def test_get_new_updates_multistream():
    product_updates_stream_name = "product_updates"
    ocr_ready_stream_name = "ocr_ready"
    base_values_product_updates = {
        "flavor": "off",
        "user_id": "user1",
        "action": "updated",
        "comment": "comment",
        "product_type": "beauty",
    }
    ocr_ready_event = {
        "product_type": "beauty",
        "code": "3215495849204",
        "image_id": "2",
        "json_url": "https://images.openfoodfacts.org/images/products/321/549/584/9204/2.json",
    }
    return_values = [
        [
            (
                product_updates_stream_name,
                [("1629878400000-0", {"code": "4", **base_values_product_updates})],
            ),
        ],
        [
            (
                ocr_ready_stream_name,
                [("1629878400001-0", ocr_ready_event)],
            ),
        ],
        [
            (
                product_updates_stream_name,
                [("1629878400002-0", {"code": "1", **base_values_product_updates})],
            )
        ],
        [
            (
                product_updates_stream_name,
                [("1629878400003-0", {"code": "2", **base_values_product_updates})],
            )
        ],
        [
            (
                product_updates_stream_name,
                [("1629878400004-0", {"code": "3", **base_values_product_updates})],
            )
        ],
    ]
    redis_client = cast(Redis, RedisXreadClient(return_values))

    # Call the function and iterate over the results
    updates_iter = get_new_updates_multistream(redis_client)

    product_update_result = next(updates_iter)
    assert product_update_result == ProductUpdateEvent(
        id="1629878400000-0",
        stream=product_updates_stream_name,
        timestamp=1629878400000,
        code="4",
        **base_values_product_updates,
    )

    ocr_ready_result = next(updates_iter)
    assert ocr_ready_result.id == "1629878400001-0"
    assert ocr_ready_result.stream == ocr_ready_stream_name
    assert ocr_ready_result.timestamp == datetime.datetime.fromtimestamp(
        1629878400.001, tz=datetime.timezone.utc
    )
    assert ocr_ready_result.code == ocr_ready_event["code"]
    assert ocr_ready_result.product_type == ocr_ready_event["product_type"]
    assert ocr_ready_result.image_id == ocr_ready_event["image_id"]
    assert ocr_ready_result.json_url == ocr_ready_event["json_url"]
