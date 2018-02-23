import random
from abc import ABC
from ai.resultChecker import ResultChecker

class AiBrain(ABC):
    """Fields: self.player, self.board, self.checker implemented in subclass - AiCtrl."""

    def __setup_fields(self):
        self.__player_symbol = self.player.get_symbol()
        self.__opponent_symbol = self.__get_opponent_symbol()
        self.__board = self.board.get_fields()
        self.__checker = ResultChecker(self.__board)
        

    def shoot_in_easy_mode(self):
        random.choice(self.__get_free_fields()).set_symbol(self.player.get_symbol())

    def shoot_in_normal_mode(self):

        self.__setup_fields()
        # todo: implement blocking opponent mechanic!

        combi = self.__select_best_combination()
        best_fields = [field for field in (combi[0], combi[2]) if field.get_symbol().isdecimal()]  # edge fields
        if best_fields:
            field = random.choice(best_fields)
        elif combi:
            field = combi[1]  # middle field
        else:  # there is no winning combination
            field = self.__get_any_free_square()

        if field:
            field.set_symbol(self.__player_symbol)

    def __select_best_combination(self):
        all_possible_combis = self.__get_best_winning_combinations()

        best_combis = [
                        combi for combi in all_possible_combis
                        if len(list(filter(lambda x: x.get_symbol() == self.__player_symbol, combi))) == 2]

        good_combis = [
                        combi for combi in all_possible_combis
                        if len(list(filter(lambda x: x.get_symbol() == self.__player_symbol, combi))) == 1]

        if best_combis:
            return random.choice(best_combis)
        elif good_combis:
            return random.choice(good_combis)
        elif all_possible_combis:
            return random.choice(all_possible_combis)

    def __get_best_winning_combinations(self):
        best_indexes = self.__checker.get_board_best_indexes_collection()
        best_combis = self.__get_possible_winning_combinations(best_indexes)
        if best_combis:
            return best_combis
        else:
            regular_indexes = self.__checker.get_board_indexes_collection()
            combis = self.__get_possible_winning_combinations(regular_indexes)
            return combis

    def __get_possible_winning_combinations(self, board_indexes_collection):
        possible_win_combis = []
        for indexes in board_indexes_collection:
            possible_win_combis.append(self.__create_combination(indexes))

        return [combi for combi in possible_win_combis if len(combi) == 3]

    def __create_combination(self, indexes):
        return [self.__board[x-1] for x in indexes if str(self.__board[x-1]) != self.__opponent_symbol]

    def __get_opponent_symbol(self):
        if self.__player_symbol == "x":
            return "o"
        return "x"

    def __get_any_free_field(self):
        free_fields = self.__get_free_fields()
        if free_fields:
            return free_fields[0]

    def __get_free_fields(self):
        return [field for field in self.__board if field.get_symbol().isdigit()]