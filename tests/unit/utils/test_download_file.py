from unittest import mock

import pytest
import requests
import requests_mock

from openfoodfacts.utils import download_file, http_session

URL = "https://static.openfoodfacts.org/data/dataset.jsonl.gz"


def test_download_file_raises_on_http_error(tmp_path):
    """download_file() must not save an HTTP error page as the dataset"""
    output_path = tmp_path / "dataset.jsonl.gz"
    with requests_mock.mock() as mock:
        mock.get(URL, status_code=404, text="Not Found")
        with pytest.raises(requests.HTTPError):
            download_file(URL, output_path, tmp_dir=tmp_path)
    assert not output_path.exists()


def test_download_file_sends_default_timeout(tmp_path):
    """download_file() must bound a stalled download with a timeout"""
    output_path = tmp_path / "dataset.jsonl.gz"
    seen = {}
    real_get = http_session.get

    def _recording_get(*args, **kwargs):
        seen.update(kwargs)
        return real_get(*args, **kwargs)

    with requests_mock.mock() as m:
        m.get(URL, text="data", headers={"Content-Length": "4"})
        with mock.patch.object(http_session, "get", side_effect=_recording_get):
            download_file(URL, output_path, tmp_dir=tmp_path)
    assert seen.get("timeout") == 10.0
    assert output_path.exists()


def test_download_file_sends_custom_timeout(tmp_path):
    """download_file() must honour an explicit timeout value"""
    output_path = tmp_path / "dataset.jsonl.gz"
    seen = {}
    real_get = http_session.get

    def _recording_get(*args, **kwargs):
        seen.update(kwargs)
        return real_get(*args, **kwargs)

    with requests_mock.mock() as m:
        m.get(URL, text="data", headers={"Content-Length": "4"})
        with mock.patch.object(http_session, "get", side_effect=_recording_get):
            download_file(URL, output_path, tmp_dir=tmp_path, timeout=42.0)
    assert seen.get("timeout") == 42.0
    assert output_path.exists()
