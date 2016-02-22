import json


class Menu(object):
    def __init__(self, menu):
        data = json.load(open(menu))
        self._menu = data[0]['prices'][0]

    def view_menu(self):
        return self._menu
