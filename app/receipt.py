import json


class Receipt(object):
    def __init__(self, order, menu):
        self._order = order
        self._menu = menu

    def receipt_as_json(self):
        receipt = {}
        for item in self._order:
            receipt[item] = "{}x ${:.2f}".format(self._order[item],
                                                 self._menu[item])
        return json.dumps(receipt)
