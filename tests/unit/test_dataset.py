import gzip

import pytest

from openfoodfacts.dataset import ProductDataset
from openfoodfacts.types import DatasetType


@pytest.mark.parametrize("prefix", ["products", "en.openfoodfacts.org.products"])
@pytest.mark.parametrize("compressed", [False, True])
@pytest.mark.parametrize(
    "extension, dataset_type, content",
    [
        ("csv", DatasetType.csv, "code\tproduct_name\n123\tExample\n"),
        ("jsonl", DatasetType.jsonl, '{"code": "123", "product_name": "Example"}\n'),
    ],
)
def test_local_dataset_format(
    tmp_path, prefix, compressed, extension, dataset_type, content
):
    path = tmp_path / f"{prefix}.{extension}{'.gz' if compressed else ''}"
    open_fn = gzip.open if compressed else open
    with open_fn(path, "wt", encoding="utf-8") as stream:
        stream.write(content)

    dataset = ProductDataset(dataset_path=path)

    assert dataset.dataset_type is dataset_type
    assert list(dataset) == [{"code": "123", "product_name": "Example"}]


@pytest.mark.parametrize(
    "filename", ["products.txt", "products.csv.zip", "products.jsonl.bak"]
)
def test_local_dataset_rejects_unknown_extension(tmp_path, filename):
    with pytest.raises(ValueError, match="Unknown dataset type"):
        ProductDataset(dataset_path=tmp_path / filename)
