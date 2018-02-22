from abc import ABC, abstractmethod


class Player(ABC):
    """Abstract class!"""

    @abstractmethod
    def __init__(self, name):
        self.name = name
        self.symbol = "-"
        self.shots = []  # contains attacked squares, eg. [1, 3, 4, 5]

    def __str__(self):
        return "{} ({})".format(self.name, self.symbol)

    def get_name(self):
        return self.name

    def set_symbol(self, symbol):
        self.symbol = symbol

    def get_symbol(self):
        return self.symbol

    def get_shots(self):
        return self.shots
