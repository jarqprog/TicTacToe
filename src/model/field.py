"""Contains square class - represents single field in game."""


class Field():

    def __init__(self, sign):
        self.symbol = '{}'.format(sign)

    def set_to_X(self):
        self.symbol = "X"

    def set_to_O(self):
        self.symbol = "O"

    def get_symbol(self):
        return self.symbol

    def __str__(self):
        return self.symbol
