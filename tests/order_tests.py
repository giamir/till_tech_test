from nose.tools import eq_
from app.order import Order


class TestOrder(object):
    def setUp(self):
        self.order = Order()

    def test_view_order_returns_current_order(self):
        eq_(self.order.view_order(), {})

    def test_ring_up_adds_item_to_order(self):
        self.order.ring_up('Mocha', 2)
        eq_(self.order.view_order(), {'Mocha': 2})

    def test_ring_up_increases_number_of_items_if_already_present(self):
        self.order.ring_up('Chai', 3)
        self.order.ring_up('Chai', 9)
        eq_(self.order.view_order(), {'Chai': 12})
