from abc import ABC, abstractmethod


class PlayerCtrl(ABC):
    """Abstract class!"""

    @abstractmethod
    def __init__(self, player, board):
        self.player = player
        self.board = board

    def get_player(self):
        return self.player

    def increment_score(self):
        self.player.set_score(self.player.get_score() + 1)

    def set_board(self, board):
        self.board = board

    @abstractmethod
    def shoot(self):
        pass
        # implement different methods for human / AI player
