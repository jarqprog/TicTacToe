from .playerCtrl import PlayerCtrl
from model.board import Board
from model.human import Human


class HumanCtrl(PlayerCtrl):

    def __init__(self, player):
        super().__init__(player)

    def get_player(self):
        return self.player

    def shoot(self):
        """Return attacked field number (in range 1 - 9)."""
        pass
        # implement different methods for human / AI player
