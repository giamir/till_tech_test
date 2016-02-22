import json
from unittest.mock import Mock
from nose.tools import eq_
from app.receipt import Receipt


class TestReceipt(object):
    def setUp(self):
        order = {'Mocha': 2, 'Chai': 3}
        menu = {'Mocha': 2.00, 'Chai': 1.00}
        self.receipt = Receipt(menu=menu, order=order)

    def test_receipt_as_json_returns_a_correct_receipt_as_json(self):
        expected_output = {
            'Mocha': '2x $2.00',
            'Chai': '3x $1.00'
        }
        eq_(self.receipt_as_json(), json.dumps(expected_output))
