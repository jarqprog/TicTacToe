from .player import Player


class Human(Player):

    def __init__(self, name, symbol):
        super().__init__(name, symbol)

    def shoot(self):
        """Return attacked field number (in range 1 - 9)."""
        return 1
