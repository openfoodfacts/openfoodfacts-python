from typing import Optional, cast

from redis import Redis

from openfoodfacts.redis import RedisUpdate, get_new_updates, get_processed_since


class RedisXrangeClient:
    def __init__(self, xrange_return_values: list):
        self.xrange_return_values = xrange_return_values
        self.call_count = 0

    def xrange(
        self, name: str, min: str = "-", max: str = "+", count: Optional[int] = None
    ):
        assert name == "product_updates_off"
        assert max == "+"
        assert count == 100
        if self.call_count >= len(self.xrange_return_values):
            return []
        self.call_count += 1
        return self.xrange_return_values[self.call_count - 1]


def test_get_processed_since():
    stream_name = "product_updates_off"
    base_values = {
        "flavor": "off",
        "user_id": "user1",
        "action": "updated",
        "comment": "comment",
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
            stream_name=stream_name,
            min_id=start_timestamp_ms,
        )
    )

    # Assertions
    assert len(results) == 2
    assert results[0] == RedisUpdate(
        id="1629878400000-0",
        stream=stream_name,
        timestamp=1629878400000,
        code="2",
        **base_values
    )
    assert results[1] == RedisUpdate(
        id="1629878400001-0",
        stream=stream_name,
        timestamp=1629878400001,
        code="3",
        **base_values
    )


class RedisXreadClient:
    def __init__(self, xread_return_values: list):
        self.xread_return_values = xread_return_values
        self.call_count = 0

    def xread(self, streams: dict, block: int, count: Optional[int] = None):
        assert set(streams.keys()) == {"product_updates_off"}
        assert block == 0
        assert count == 100
        if self.call_count >= len(self.xread_return_values):
            raise ValueError("No more values")
        self.call_count += 1
        return self.xread_return_values[self.call_count - 1]


def test_get_new_updates():
    redis_stream_name = "product_updates_off"
    base_values = {
        "flavor": "off",
        "user_id": "user1",
        "action": "updated",
        "comment": "comment",
    }
    return_values = [
        [
            (
                redis_stream_name,
                [("1629878400002-0", {"code": "4", **base_values})],
            )
        ],
        [
            (
                redis_stream_name,
                [("1629878400000-0", {"code": "1", **base_values})],
            )
        ],
        [
            (
                redis_stream_name,
                [("1629878400001-0", {"code": "2", **base_values})],
            )
        ],
        [
            (
                redis_stream_name,
                [("1629878400003-0", {"code": "3", **base_values})],
            )
        ],
    ]
    redis_client = cast(Redis, RedisXreadClient(return_values))

    # Call the function and iterate over the results
    updates_iter = get_new_updates(redis_client, stream_name=redis_stream_name)

    results = next(updates_iter)
    assert results == RedisUpdate(
        id="1629878400002-0",
        stream=redis_stream_name,
        timestamp=1629878400002,
        code="4",
        **base_values
    )
