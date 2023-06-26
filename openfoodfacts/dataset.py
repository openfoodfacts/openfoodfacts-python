import csv
import json
import shutil
import time
from pathlib import Path
from typing import Optional

import tqdm

from .types import DatasetType, Environment, Flavor
from .utils import URLBuilder, get_logger, get_open_fn, http_session, jsonl_iter

logger = get_logger(__name__)


CACHE_DIR = Path("~/.cache/openfoodfacts/datasets").expanduser()
DATASET_FILE_NAMES = {
    DatasetType.jsonl: "openfoodfacts-products.jsonl.gz",
    DatasetType.csv: "en.openfoodfacts.org.products.csv.gz",
}

JSONL_DATASET_FILE_PATHS = {
    DatasetType.jsonl: CACHE_DIR / DATASET_FILE_NAMES[DatasetType.jsonl],
    DatasetType.csv: CACHE_DIR / DATASET_FILE_NAMES[DatasetType.csv],
}


def sanitize_file_path(file_path: Path, suffix: str) -> Path:
    return file_path.with_name(file_path.name.replace(".", "_") + suffix)


def fetch_etag(url: str) -> str:
    """Get the Etag of a remote file.

    :param url: the file URL
    :return: the Etag
    """
    r = http_session.head(url)
    return r.headers.get("ETag", "").strip("'\"")


def download_file(url: str, output_path: Path):
    """Download a dataset file and store it in `output_path`.

    The dataset metadata (`etag`, `url`, `created_at`) are stored in a JSON
        file whose name is derived from `output_path`
    :param url: the file URL
    :param output_path: the file output path
    """
    r = http_session.get(url, stream=True)
    etag = r.headers.get("ETag", "").strip("'\"")

    tmp_output_path = output_path.with_name(output_path.name + ".part")
    with tmp_output_path.open("wb") as f, tqdm.tqdm(
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
        miniters=1,
        desc=str(output_path),
        total=int(r.headers.get("content-length", 0)),
    ) as pbar:
        for chunk in r.iter_content(chunk_size=4096):
            f.write(chunk)
            pbar.update(len(chunk))

    shutil.move(tmp_output_path, output_path)

    sanitize_file_path(output_path, ".json").write_text(
        json.dumps(
            {
                "etag": etag,
                "created_at": int(time.time()),
                "url": url,
            }
        )
    )


def get_dataset_etag(dataset_path: Path) -> Optional[str]:
    """Return a dataset Etag.

    :param dataset_path: the path of the dataset
    :return: the file Etag
    """
    metadata_path = sanitize_file_path(dataset_path, ".json")

    if metadata_path.is_file():
        return json.loads(metadata_path.read_text())["etag"]

    return None


def get_dataset(
    dataset_type: DatasetType = DatasetType.jsonl,
    force_download: bool = False,
    download_newer: bool = False,
) -> Path:
    """Download (and cache) Open Food Facts dataset.

    The dataset is downloaded the first time and subsequently cached in
    `~/.cache/openfoodfacts/datasets`.

    :param dataset_type: The, defaults to DatasetType.jsonl
    :param force_download: if True, (re)download the dataset even if it was
        cached, defaults to False
    :param download_newer: if True, download the dataset if a more recent
        version is available (based on file Etag)
    :return: the path of the dataset
    """
    dataset_path = JSONL_DATASET_FILE_PATHS[dataset_type]
    file_name = DATASET_FILE_NAMES[dataset_type]
    url = f"{URLBuilder.static(Flavor.off, Environment.org)}/data/{file_name}"

    if dataset_path.is_file():
        if not force_download:
            return dataset_path

        if download_newer:
            cached_etag = get_dataset_etag(dataset_path)
            current_etag = fetch_etag(url)

            if cached_etag == current_etag:
                # The file is up to date, return cached file path
                return dataset_path

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    logger.info("Downloading dataset, saving it in %s", dataset_path)
    download_file(url, dataset_path)
    return dataset_path


class ProductDataset:
    def __init__(self, dataset_type: DatasetType = DatasetType.jsonl, **kwargs):
        """A product dataset.

        This class is used to iterate over the Open Food Facts dataset.

        :param dataset_type: the dataset type to use (csv or jsonl), defaults
            to DatasetType.jsonl
        """
        self.dataset_type = dataset_type
        self.dataset_path = get_dataset(dataset_type, **kwargs)

    def __iter__(self):
        if self.dataset_type is DatasetType.jsonl:
            return jsonl_iter(self.dataset_path)
        else:
            return self._csv_iterator()

    def _csv_iterator(self):
        open_fn = get_open_fn(self.dataset_path)
        with open_fn(self.dataset_path, "rt", newline="") as csvfile:
            reader = csv.DictReader(csvfile, delimiter="\t")
            for row in reader:
                yield dict(row)

    def count(self) -> int:
        """Return the number of products in the dataset."""
        count = 0
        for _ in self:
            count += 1

        return count
