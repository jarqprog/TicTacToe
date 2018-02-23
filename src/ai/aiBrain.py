from .checker import Checker
import random


class AiBrain(Checker):

    # implement ai methods
    def shoot_in_easy_mode(self):
        random.choice(self.__get_free_fields()).set_symbol(self.player.get_symbol())

    def shoot_in_normal_mode(self):
        pass

    def shoot_in_hard_mode(self):
        pass

    def __get_free_fields(self):
        return [field for field in self.board.get_fields() if field.get_symbol().isdigit()]
