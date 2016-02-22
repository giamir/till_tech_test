from nose.tools import eq_
from app.till import Till


class TestStories(object):
    def setUp(self):
        self.till = Till()

    def test_janes_order(self):
        # Jane wishes to make the following order
        janes_order = {
            'Cafe Latte': 2,
            'Blueberry Muffin': 1,
            'Choc Mudcake': 1
        }
        self.till.ring_up('Cafe Latte', 2)
        self.till.ring_up('Blueberry Muffin', 1)
        self.till.ring_up('Choc Mudcake', 1)
        eq_(self.till.preview_order(), janes_order)
