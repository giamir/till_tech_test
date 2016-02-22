from app.order import Order
from forwardable import def_delegator


class Till(object):
    def __init__(self, menu, order_klass=Order):
        self._menu = menu
        self._order_klass = order_klass
        self._current_order = self._order_klass()

    def_delegator('_current_order', 'view_order')

    def ring_up(self, item, quantity):
        self._current_order.ring_up(item, quantity)
