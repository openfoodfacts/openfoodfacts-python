from io import BytesIO
from unittest.mock import Mock

import pytest
import requests
import requests_mock

from openfoodfacts import utils
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


@pytest.mark.parametrize("failure", [None, "http", "stream", "move"])
def test_download_file_cleans_up_resources(tmp_path, monkeypatch, failure):
    output_path = tmp_path / "dataset.jsonl.gz"
    output_path.write_bytes(b"previous dataset")
    metadata_path = tmp_path / "dataset_jsonl_gz.json"
    metadata_path.write_text("previous metadata")
    temporary_parent = tmp_path / "downloads"
    temporary_parent.mkdir()
    unrelated = temporary_parent / "keep.txt"
    unrelated.write_text("keep")

    response = requests.Response()
    response.status_code = 404 if failure == "http" else 200
    response.headers["ETag"] = '"dataset-etag"'
    response.raw = BytesIO(b"new dataset")
    response.close = Mock(wraps=response.close)
    monkeypatch.setattr(utils.http_session, "get", Mock(return_value=response))

    if failure == "stream":

        def interrupted_stream(chunk_size):
            yield b"partial dataset"
            raise requests.ConnectionError("download interrupted")

        monkeypatch.setattr(response, "iter_content", interrupted_stream)
    elif failure == "move":
        monkeypatch.setattr(
            utils.shutil, "move", Mock(side_effect=OSError("cannot move download"))
        )

    if failure is None:
        download_file(URL, output_path, tmp_dir=temporary_parent)
        assert output_path.read_bytes() == b"new dataset"
        assert utils.get_file_etag(output_path) == "dataset-etag"
    else:
        exception = {
            "http": requests.HTTPError,
            "stream": requests.ConnectionError,
            "move": OSError,
        }[failure]
        with pytest.raises(exception):
            download_file(URL, output_path, tmp_dir=temporary_parent)
        assert output_path.read_bytes() == b"previous dataset"
        assert metadata_path.read_text() == "previous metadata"

    assert list(temporary_parent.iterdir()) == [unrelated]
    response.close.assert_called_once()


def test_download_file_creates_temporary_parent(tmp_path):
    temporary_parent = tmp_path / "nested" / "downloads"
    output_path = tmp_path / "dataset.jsonl.gz"
    with requests_mock.mock() as mock:
        mock.get(URL, content=b"dataset")
        download_file(URL, output_path, tmp_dir=temporary_parent)
    assert output_path.read_bytes() == b"dataset"
    assert list(temporary_parent.iterdir()) == []
