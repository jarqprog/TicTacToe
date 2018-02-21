"""Contains square class - represents single field in game."""


class Square():

    def __init__(self, id):
        self.id = id
        self.symbol = ' {} '.format(self.id)

    def set_to_X(self):
        self.symbol = " X "

    def set_to_O(self):
        self.symbol = " O "

    def get_id(self):
        return self.id

    def get_symbol(self):
        return self.symbol

    def __str__(self):
        return self.symbol
