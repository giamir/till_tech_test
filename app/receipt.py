import json


class Receipt(object):
    def __init__(self, order, menu):
        self._order = order
        self._menu = menu

    def receipt_as_json(self):
        receipt = {}
        for item in self._order:
            receipt[item] = self._calculate_line(item)
        receipt['Tax'] = '${:.2f}'.format(self._calculate_tax())
        receipt['Total'] = '${:.2f}'.format(self._gross_total())
        return json.dumps(receipt)

    def _net_total(self):
        total = 0
        for item in self._order:
            total += self._order[item] * self._menu[item]
        return total

    def _calculate_tax(self):
        return self._net_total() * 0.0864

    def _gross_total(self):
        return self._net_total() + self._calculate_tax()

    def _calculate_line(self, item):
        return '{}x ${:.2f}'.format(self._order[item], self._menu[item])
