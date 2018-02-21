from abc import ABC, abstractmethod


class PlayerCtrl(ABC):
    """Abstract class!"""

    @abstractmethod
    def __init__(self, player):
        self.player = player

    def get_player(self):
        return self.player

    @abstractmethod
    def shoot(self):
        """Return attacked field number (in range 1 - 9)."""
        pass
        # implement different methods for human / AI player 

