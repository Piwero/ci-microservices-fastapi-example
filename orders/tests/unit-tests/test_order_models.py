from orders.models import Order


class TestOrderModel:
    def test_product_has_id_field(self):
        order: Order = Order()

        assert order.id

