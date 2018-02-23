from .playerCtrl import PlayerCtrl
from view.playerView import PlayerView


class HumanCtrl(PlayerCtrl):

    def __init__(self, player, board):
        super().__init__(player, board)
        self.view = PlayerView()

    def shoot(self):
        symbol = self.player.get_symbol()
        fields = self.board.get_fields()
        correct_choices = [str(field) for field in fields if field not in ("x", "o")]
        field_index = int(self.view.get_field_number_to_shoot(correct_choices))
        self.board.change_field(field_index, symbol)
