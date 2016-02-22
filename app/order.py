class Order(object):
    def __init__(self):
        self._items = {}

    def view(self):
        return self._items

    def add_item(self, item, quantity):
        if item in self._items:
            self._items[item] += quantity
        else:
            self._items[item] = quantity
