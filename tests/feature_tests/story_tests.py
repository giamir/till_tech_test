import json
from nose.tools import eq_
from app.till import Till
from app.menu import Menu


class TestStories(object):
    def setUp(self):
        menu = Menu('data/hipstercoffee.json')
        self.till = Till(menu=menu)

    def test_janes_order_receipt_as_json(self):
        # Jane wishes to make the following order
        janes_order = {
            'Cafe Latte': 2,
            'Blueberry Muffin': 1,
            'Choc Mudcake': 1
        }
        self.till.ring_up('Cafe Latte', 2)
        self.till.ring_up('Blueberry Muffin', 1)
        self.till.ring_up('Choc Mudcake', 1)
        eq_(self.till.view_order(), janes_order)

        expected_output = {
            'Cafe Latte': '2x $4.75',
            'Blueberry Muffin': '1x $4.05',
            'Choc Mudcake': '1x $6.40'
        }
        eq_(self.till.receipt_as_json(), json.dumps(expected_output))
