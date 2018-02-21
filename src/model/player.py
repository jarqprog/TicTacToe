from abc import ABC, abstractmethod


class Player(ABC):
    """Abstract class!"""

    @abstractmethod
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.shots = []  # contains attacked squares, eg. [1, 3, 4, 5]

    def __str__(self):
        return "Player\n\t\tname: {} \n\t\tsymbol: {}".format(self.name, self.symbol)

    def get_name(self):
        return self.name

    def get_symbol(self):
        return self.symbol

    def get_shots(self):
        return self.shots
