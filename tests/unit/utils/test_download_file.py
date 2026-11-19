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


def test_download_file_removes_tmp_dir_on_success(tmp_path):
    """download_file() must not leave its per-download temporary directory behind"""
    output_path = tmp_path / "dataset.jsonl.gz"
    with requests_mock.mock() as m:
        m.get(URL, text="data", headers={"Content-Length": "4"})
        download_file(URL, output_path, tmp_dir=tmp_path)
    assert output_path.exists()
    assert list(tmp_path.glob("tmp_off_*")) == []


def test_download_file_removes_tmp_dir_on_streaming_failure(tmp_path):
    """download_file() must clean up the partial download when streaming fails"""
    output_path = tmp_path / "dataset.jsonl.gz"

    class _FailingResponse:
        headers = {"Content-Length": "4", "ETag": "abc"}

        def raise_for_status(self):
            return None

        def iter_content(self, chunk_size=4096):
            yield b"da"
            raise requests.exceptions.Timeout("stalled download")

    with mock.patch.object(http_session, "get", return_value=_FailingResponse()):
        with pytest.raises(requests.exceptions.Timeout):
            download_file(URL, output_path, tmp_dir=tmp_path)
    assert not output_path.exists()
    assert list(tmp_path.glob("tmp_off_*")) == []


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
