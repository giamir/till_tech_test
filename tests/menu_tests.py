from nose.tools import eq_, raises, assert_raises_regexp
from app.menu import Menu, NotInMenuError
import json


class TestMenu(object):
    def setUp(self):
        data = json.load(open('data/hipstercoffee.json'))
        self.price_data = data[0]['prices'][0]
        self.menu = Menu('data/hipstercoffee.json')

    def test_view_menu_returns_the_menu(self):
        eq_(self.menu.view_menu(), self.price_data)

    def test_price_returns_the_price_of_item_requested(self):
        eq_(self.menu.price('Cafe Latte'), self.price_data['Cafe Latte'])

    @raises(NotInMenuError)
    def test_price_raises_exception_if_item_is_not_in_menu(self):
        self.menu.price('item not in menu')

    @raises(NotInMenuError)
    def test_verify_in_menu_raises_NotInMenuError_if_item_is_not_in_menu(self):
        self.menu.verify_in_menu('item not in menu')


class TestNotInMenuError(object):
    def raise_error(self):
        raise NotInMenuError('Mocha Chai')

    def test_when_raised_has_descriptive_string(self):
        assert_raises_regexp(NotInMenuError,
                             'Mocha Chai is not in this menu',
                             self.raise_error)
