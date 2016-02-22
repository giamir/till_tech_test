from unittest.mock import Mock
from nose.tools import raises
from app.till import Till
from app.menu import NotInMenuError

class TestTill(object):
    def setUp(self):
        menu_mock = Mock(view_menu=['Menu Item'])
        self.order_mock = Mock()
        self.order_klass_mock = Mock(return_value=self.order_mock)
        self.till = Till(menu=menu_mock, order_klass=self.order_klass_mock)

    def test_till_delegates_view_order_to_order(self):
        self.till.view_order()
        self.order_mock.view_order_assert_called()

    def test_till_delegates_ring_up_to_order_if_item_in_menu(self):
        self.till.ring_up('Menu Item', 2)
        self.order_mock.ring_up.assert_called_with('Menu Item', 2)

    @raises(NotInMenuError)
    def test_till_raises_NotInMenuError_if_item_not_in_menu(self):
        self.till.ring_up('Nonexistant Item', 3)
