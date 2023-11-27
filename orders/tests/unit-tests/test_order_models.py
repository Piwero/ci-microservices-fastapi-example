import pytest

from inventory.inventory.models import Product
from orders.models import Order, OrderItem


@pytest.fixture
def product_1():
    product: Product = Product(name="Product 1", price=30.99)
    return product


class TestOrderItem:
    def test_order_item_has_product_field(self, product_1):
        order_item = OrderItem(product=product_1)

        assert order_item.product == product_1


class TestOrderModel:
    def test_product_has_id_field(self):
        order: Order = Order()

        assert order.id
