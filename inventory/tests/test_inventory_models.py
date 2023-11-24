from decimal import Decimal

import pytest
from pydantic import ValidationError

from inventory.models import Product


def test_product_has_name_field():
    product: Product = Product(name="Product 1")

    assert product.name == "Product 1"


def test_product_has_price_field():
    product: Product = Product(name="Product 1", price=Decimal(100.50))

    assert product.price == 100.50


def test_product_cannot_have_negative_price():
    with pytest.raises(ValidationError):
        Product(name="Product 1", price=Decimal(-100.50))
