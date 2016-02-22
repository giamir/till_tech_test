from nose.tools import eq_
from app.order import Order


class TestOrder(object):
    def setUp(self):
        self.order = Order()

    def test_view_returns_current_order(self):
        eq_(self.order.view, [])
