from nose.tools import eq_
from app.menu import Menu
import json


class TestMenu(object):
    def setUp(self):
        data = json.load(open('data/hipstercoffee.json'))
        self.price_data = data[0]['prices'][0]
        self.menu = Menu('data/hipstercoffee.json')

    def test_view_menu_returns_the_menu(self):
        eq_(self.menu.view_menu(), self.price_data)
