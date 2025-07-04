import io
from pathlib import Path
from unittest.mock import patch

import pytest
import requests
from PIL import Image

from openfoodfacts.utils import (
    AssetLoadingException,
    get_image_from_url,
    should_download_file,
)


def test_get_image_from_url(requests_mock):
    # Test case 1: Valid image URL
    image_url = "https://example.com/image.jpg"

    f = io.BytesIO()
    # Create a white image file
    Image.new("RGB", (100, 100), "white").save(f, format="JPEG")
    f.seek(0)
    image_data = f.read()
    requests_mock.get(image_url, content=image_data)
    image = get_image_from_url(image_url)
    assert isinstance(image, Image.Image)

    struct = get_image_from_url(image_url, return_struct=True)
    assert struct.url == image_url
    assert struct.response is not None and struct.response.status_code == 200
    assert struct.image == image

    # Test case 2: Invalid image URL
    invalid_image_url = "https://example.com/invalid_image.jpg"
    requests_mock.get(invalid_image_url, content=b"invalid-image")
    with pytest.raises(AssetLoadingException):
        get_image_from_url(invalid_image_url)

    # Same with error_raise=False
    assert get_image_from_url(invalid_image_url, error_raise=False) is None

    # Same thing with struct
    struct = get_image_from_url(
        invalid_image_url, return_struct=True, error_raise=False
    )
    assert struct.url == invalid_image_url
    assert struct.response is not None and struct.response.status_code == 200
    assert struct.image is None
    assert struct.error == "Cannot identify image https://example.com/invalid_image.jpg"

    # Test case 3: Image URL with connection error
    connection_error_url = "https://example.com/connection_error.jpg"
    requests_mock.get(connection_error_url, exc=requests.exceptions.ConnectionError)
    with pytest.raises(AssetLoadingException):
        get_image_from_url(connection_error_url)

    # Same but with error_raise=False
    assert get_image_from_url(connection_error_url, error_raise=False) is None

    # Same but with return_struct=True
    struct = get_image_from_url(
        connection_error_url, return_struct=True, error_raise=False
    )
    assert struct.url == connection_error_url
    assert struct.response is None
    assert struct.image is None
    assert struct.error == "Cannot download https://example.com/connection_error.jpg"

    # Test case 4: Image URL with HTTP error
    http_error_url = "https://example.com/http_error.jpg"
    requests_mock.get(http_error_url, status_code=404)
    with pytest.raises(AssetLoadingException):
        get_image_from_url(http_error_url)


def test_should_download_file():
    url = "https://example.com/file"
    filepath = Path("/path/to/file")

    # Test case 1: File does not exist
    with patch.object(Path, "is_file", return_value=False):
        assert (
            should_download_file(
                url, filepath, force_download=False, download_newer=False
            )
            is True
        )

    # Test case 2: Force download
    with patch.object(Path, "is_file", return_value=True):
        assert (
            should_download_file(
                url, filepath, force_download=True, download_newer=False
            )
            is True
        )

    # Test case 3: Download newer with same ETag
    with (
        patch.object(Path, "is_file", return_value=True),
        patch("openfoodfacts.utils.get_file_etag", return_value="etag123"),
        patch("openfoodfacts.utils.fetch_etag", return_value="etag123"),
    ):
        assert (
            should_download_file(
                url, filepath, force_download=False, download_newer=True
            )
            is False
        )

    # Test case 4: Download newer with different ETag
    with (
        patch.object(Path, "is_file", return_value=True),
        patch("openfoodfacts.utils.get_file_etag", return_value="etag123"),
        patch("openfoodfacts.utils.fetch_etag", return_value="etag456"),
    ):
        assert (
            should_download_file(
                url, filepath, force_download=False, download_newer=True
            )
            is True
        )

    # Test case 5: No force download and no download newer, the file
    # exists so we don't download it again
    with patch.object(Path, "is_file", return_value=True):
        assert (
            should_download_file(
                url, filepath, force_download=False, download_newer=False
            )
            is False
        )
