import pytest
import requests
import requests_mock

from openfoodfacts.utils import download_file

URL = "https://static.openfoodfacts.org/data/dataset.jsonl.gz"


def test_download_file_raises_on_http_error(tmp_path):
    """download_file() must not save an HTTP error page as the dataset"""
    output_path = tmp_path / "dataset.jsonl.gz"
    with requests_mock.mock() as mock:
        mock.get(URL, status_code=404, text="Not Found")
        with pytest.raises(requests.HTTPError):
            download_file(URL, output_path, tmp_dir=tmp_path)
    assert not output_path.exists()
