import json


class Receipt(object):
    def __init__(self, order, menu):
        self._order = order
        self._menu = menu

    def receipt_as_json(self):
        receipt = {}
        total = 0
        for item in self._order:
            receipt[item] = "{}x ${:.2f}".format(self._order[item],
                                                 self._menu[item])
            total += self._order[item] * self._menu[item]
        receipt['Tax'] = "${:.2f}".format(total * 0.0864, 2)
        return json.dumps(receipt)
