from unittest.mock import Mock
from nose.tools import eq_
from app.till import Till


class TestTill(object):
    def setUp(self):
        menu_mock = Mock()
        self.order_klass_mock = Mock()
        self.till = Till(menu=menu_mock, order_klass=self.order_klass_mock)

    def test_till_delegates_ring_up_to_order(self):
        self.till.ring_up('Menu Item', 2)
        self.order_klass_mock.ring_up.assert_called_with('Menu Item', 2)
