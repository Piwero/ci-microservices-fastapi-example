from orders.models import Order


def test_product_has_id_field():
    order: Order = Order()

    assert order.id
