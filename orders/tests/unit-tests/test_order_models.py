import pytest

from inventory.models import Product
from orders.models import Order, OrderItem


@pytest.fixture
def product_1():
    product: Product = Product(name="Product 1", price=30.99)
    return product


@pytest.fixture
def product_2():
    product: Product = Product(name="Product 2", price=120.99)
    return product


class TestOrderItem:
    def test_order_item_has_product_field(self, product_1):
        order_item = OrderItem(product=product_1)

        assert order_item.product == product_1


class TestOrderModel:
    def test_order_has_id_field(self):
        order: Order = Order()

        assert order.id

    def test_order_can_be_without_products(self):
        order: Order = Order()

        assert order

    def test_order_can_have_one_item(self, product_1):
        order_item_1: OrderItem = OrderItem(product=product_1)

        order: Order = Order(items=[order_item_1])

        assert len(order.items) == 1
        assert order.items[0] == order_item_1
        assert order.items[0].product == product_1

    def test_order_can_have_many_items(self, product_1, product_2):
        order_item_1: OrderItem = OrderItem(product=product_1)
        order_item_2: OrderItem = OrderItem(product=product_2)

        order: Order = Order(items=[order_item_1, order_item_2])

        assert len(order.items) == 2
        assert order.items[0] == order_item_1
        assert order.items[1] == order_item_2
        assert order.items[0].product == product_1
        assert order.items[1].product == product_2
