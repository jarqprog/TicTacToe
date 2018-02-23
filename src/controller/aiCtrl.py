from .playerCtrl import PlayerCtrl
from exception.customException import CustomException
from model.ai import Ai
from ai.aiBrain import AiBrain


class AiCtrl(PlayerCtrl, AiBrain):

    def __init__(self, player, board, difficulty_level):
        if not isinstance(player, Ai):
            raise CustomException("wrong type!")
        if difficulty_level not in ("easy", "normal", "hard"):
            raise CustomException("there is no such difficulty level!")
        super().__init__(player, board)
        self.intelligence = difficulty_level

    def get_player(self):
        return self.player

    def shoot(self):
        if self.intelligence == "easy":
            self.shoot_in_easy_mode()
        elif self.intelligence == "normal":
            pass
        else:
            pass

    def __shoot_in_easy_mode(self):
        pass

    def __shoot_in_normal_mode(self):
        pass

    def __shoot_in_hard_mode(self):
        pass
