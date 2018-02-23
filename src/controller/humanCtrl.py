from .playerCtrl import PlayerCtrl
from view.playerView import PlayerView
from exception.customException import CustomException
from model.human import Human


class HumanCtrl(PlayerCtrl):

    def __init__(self, player, board):
        if not isinstance(player, Human):
            raise CustomException("wrong type!")
        super().__init__(player, board)
        self.view = PlayerView()

    def get_player(self):
        return self.player

    def shoot(self):
        symbol = self.player.get_symbol()
        fields = self.board.get_fields()
        correct_choices = [str(field) for field in fields if field not in ("x", "o")]
        field_index = int(self.view.get_field_number_to_shoot(correct_choices))
        self.board.change_field(field_index, symbol)
