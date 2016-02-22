from nose.tools import eq_
from app.order import Order


class TestOrder(object):
    def setUp(self):
        self.order = Order()

    def test_view_returns_current_order(self):
        eq_(self.order.view(), {})

    def test_add_item_adds_item_to_order(self):
        self.order.add_item('Mocha', 2)
        eq_(self.order.view(), {'Mocha': 2})
