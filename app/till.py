from app.order import Order
from app.receipt import Receipt
from forwardable import def_delegator


class Till(object):
    def __init__(self, menu, order_klass=Order, receipt_klass=Receipt):
        self._menu = menu
        self._order_klass = order_klass
        self._current_order = self._order_klass()
        self._receipt_klass = receipt_klass

    def_delegator('_current_order', 'view_order')

    def ring_up(self, item, quantity):
        self._menu.verify_in_menu(item)
        self._current_order.ring_up(item, quantity)

    def receipt_as_json(self):
        receipt = self._receipt_klass(self._current_order.view_order(),
                                      self._menu.view_menu())
        return receipt.receipt_as_json()
