"""Contains square class - represents single field in game."""


class Field():

    def __init__(self, sign):
        self.symbol = '{}'.format(sign)

    def set_symbol(self, symbol):
        self.symbol = symbol

    def get_symbol(self):
        return self.symbol

    def __str__(self):
        return self.symbol
