import gzip
from functools import partial

import pytest

from openfoodfacts import dataset
from openfoodfacts.dataset import ProductDataset


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
