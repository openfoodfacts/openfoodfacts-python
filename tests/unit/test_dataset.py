import gzip
from functools import partial

import pytest

from openfoodfacts import dataset
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


@pytest.mark.parametrize("compressed", [False, True])
@pytest.mark.parametrize("default_encoding", ["ascii", "cp1252"])
def test_csv_uses_utf8_independently_of_locale(
    tmp_path, monkeypatch, compressed, default_encoding
):
    path = tmp_path / ("products.csv.gz" if compressed else "products.csv")
    contents = 'code\tproduct_name\n12345678\t"Crème brûlée\n咖啡"\n'
    if compressed:
        with gzip.open(path, "wt", encoding="utf-8", newline="") as stream:
            stream.write(contents)
    else:
        path.write_text(contents, encoding="utf-8", newline="")

    original_get_open_fn = dataset.get_open_fn
    monkeypatch.setattr(
        dataset,
        "get_open_fn",
        lambda path: partial(original_get_open_fn(path), encoding=default_encoding),
    )

    products = ProductDataset(dataset_path=path)
    assert list(products) == [
        {"code": "12345678", "product_name": "Crème brûlée\n咖啡"}
    ]
    assert products.count() == 1
