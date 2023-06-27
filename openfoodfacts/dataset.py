import csv
from pathlib import Path

from .types import DatasetType, Environment, Flavor
from .utils import (
    URLBuilder,
    download_file,
    get_logger,
    get_open_fn,
    jsonl_iter,
    should_download_file,
)

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

    if not should_download_file(url, dataset_path, force_download, download_newer):
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
