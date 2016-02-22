import json


class Receipt(object):
    def __init__(self, order, menu):
        self._order = order
        self._menu = menu

    def receipt_as_json(self):
        receipt = {}
        for item in self._order:
            receipt[item] = self._calculate_line(item)
        receipt['Tax'] = self._calculate_tax()
        return json.dumps(receipt)

    def _sum_order(self):
        total = 0
        for item in self._order:
            total += self._order[item] * self._menu[item]
        return total

    def _calculate_tax(self):
        tax = self._sum_order() * 0.0864
        return "${:.2f}".format(tax)

    def _calculate_line(self, item):
        return "{}x ${:.2f}".format(self._order[item], self._menu[item])
