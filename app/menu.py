import json


class Menu(object):
    def __init__(self, menu):
        data = json.load(open(menu))
        self._menu = data[0]['prices'][0]

    def view_menu(self):
        return self._menu

    def price(self, item):
        if item not in self._menu:
            raise NotInMenuError(item)
        return self._menu[item]


class NotInMenuError(RuntimeError):
    def __init__(self, item):
        RuntimeError.__init__(self, "{} is not in this menu".format(item))
