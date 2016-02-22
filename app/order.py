class Order(object):
    def __init__(self):
        self._items = {}

    def view_order(self):
        return self._items

    def ring_up(self, item, quantity):
        if item in self._items:
            self._items[item] += quantity
        else:
            self._items[item] = quantity
