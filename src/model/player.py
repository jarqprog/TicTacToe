from abc import ABC, abstractmethod
from exception.customException import CustomException


class Player(ABC):
    """Abstract class!"""

    @abstractmethod
    def __init__(self, name, symbol):
        self.name = name
        if symbol not in ("x", "o"):
            raise CustomException("wrong symbol! (symbol should be 'x' or 'o')")

        self.symbol = symbol
        self.shots = []  # contains attacked squares, eg. [1, 3, 4, 5]

    def __str__(self):
        return "{} ({})".format(self.name, self.symbol)

    def get_name(self):
        return self.name

    def get_symbol(self):
        return self.symbol

    def get_shots(self):
        return self.shots
