from .playerCtrl import PlayerCtrl
from exception.customException import CustomException
from ai.aiBrain import AiBrain


class AiCtrl(PlayerCtrl, AiBrain):

    def __init__(self, player, board, difficulty_level):
        if difficulty_level not in ("easy", "normal", "hard"):
            raise CustomException("there is no such difficulty level!")
        super().__init__(player, board)
        self.difficulty_level = difficulty_level

    def get_player(self):
        return self.player

    def shoot(self):
        self.attack_field()
