import random
from abc import ABC
from ai.resultChecker import ResultChecker


class AiBrain(ABC):
    """Fields: self.player, self.board, self.checker implemented in subclass - AiCtrl."""

    MIDDLE_FIELD_NUMBER = 5

    def __setup_fields(self):
        self.__player_symbol = self.player.get_symbol()
        self.__opponent_symbol = self.__get_opponent_symbol()
        self.__fields = self.board.get_fields()
        self.__checker = ResultChecker(self.board)
        self.__is_in_draw_mode = False
        self.__is_player_moving_first = False

    def shoot_in_easy_mode(self):
        self.__setup_fields()
        self.__select_best_field_to_attack_easy_mode()

    def shoot_in_normal_mode(self):
        self.__setup_fields()
        self.__select_best_field_to_attack_normal_mode()

    def shoot_in_hard_mode(self):
        self.__setup_fields()
        self.__select_best_field_to_attack_hard_mode()

    def __select_best_field_to_attack_easy_mode(self):
        field = self.__try_to_get_field_to_win_or_block()
        if not field:
            field = random.choice(self.__get_free_fields())   # get field by random choice
        if field:
            field.set_symbol(self.__player_symbol)

    def __select_best_field_to_attack_normal_mode(self):
        field = self.__try_to_get_field_to_win_or_block()  # get field that wins or blocks opponent
        if not field:
            combi = self.__select_best_combination()
            if combi:
                best_fields = [field for field in (combi[0], combi[2]) if field.get_symbol().isdecimal()]  # edge fields
                if best_fields:
                    field = random.choice(best_fields)
                else:
                    field = combi[1]  # middle field
            else:  # there is no winning combination, get anything
                field = self.__get_any_free_field()

        if field:
            field.set_symbol(self.__player_symbol)

    def __select_best_field_to_attack_hard_mode(self):

        self.__is_player_moving_first = self.__check_if_player_moving_first()
        field = self.__try_to_get_field_to_win_or_block()  # get field that wins or blocks opponent
        if not field:
            field = self.__try_to_get_middle_field()  # if it's second player, try 'draw' strategy
        if not field:
            field = self.__try_to_get_field_to_block_opposite_corner_tactic()
        if not field:
            combi = self.__select_best_combination()
            if combi:
                best_fields = [field for field in (combi[0], combi[2]) if field.get_symbol().isdecimal()]  # edge fields
                if best_fields:
                    field = random.choice(best_fields)
                else:
                    field = combi[1]  # middle field
            else:  # there is no winning combination, get anything
                field = self.__get_any_free_field()

        if field:
            field.set_symbol(self.__player_symbol)

    def __select_best_combination(self):
        all_possible_combis = self.__get_best_winning_combinations()

        better_combis = [
                        combi for combi in all_possible_combis
                        if len(list(filter(lambda x: x.get_symbol() == self.__player_symbol, combi))) == 1]

        if better_combis:
            return random.choice(better_combis)

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

        return [combi for combi in possible_win_combis
                if len(combi) == 3]  # avoid lost combination where opponent has symbol

    def __create_combination(self, indexes):
        return [self.__fields[x-1] for x in indexes if str(self.__fields[x-1]) != self.__opponent_symbol]

    def __get_opponent_symbol(self):
        if self.__player_symbol == "x":
            return "o"
        return "x"

    def __get_any_free_field(self):
        free_fields = self.__get_free_fields()
        if free_fields:
            return free_fields[0]

    def __get_free_fields(self):
        return [field for field in self.__fields if field.get_symbol().isdigit()]

    def __try_to_get_field_to_win_or_block(self):
        field = self.__try_to_get_winning_field_of_given_player(self.__player_symbol)
        if not field:
            field = self.__try_to_get_winning_field_of_given_player(self.__opponent_symbol)
        return field

    def __try_to_get_winning_field_of_given_player(self, player_symbol):
        """For win or block opponent."""
        free_fields = self.__get_free_fields()
        for field in free_fields:
            current_symbol = field.get_symbol()
            field.set_symbol(player_symbol)
            if self.__checker.check_if_won(player_symbol):
                field.set_symbol(current_symbol)
                return field
            field.set_symbol(current_symbol)

    # def __try_to_get_opposite_corner_field(self):
    #     if self.__is_player_moving_first & self.__check_if_is_second_round():

    def __try_to_get_middle_field(self):
        cond_1 = (not self.__is_player_moving_first)
        cond_2 = self.__check_if_is_initial_round()
        if cond_1 & cond_2:
            return self.__try_to_get_unoccupied_field_by_number(self.MIDDLE_FIELD_NUMBER)

    def __try_to_get_field_to_block_opposite_corner_tactic(self):
        cond_1 = (not self.__is_player_moving_first)
        cond_2 = self.__check_if_is_second_round()
        if cond_1 & cond_2:
            if self.__check_if_opponent_attacked_opposite_corners():
                cross_fields_numbers = [2, 4, 6, 8]
                random.shuffle(cross_fields_numbers)
                for num in cross_fields_numbers:
                    cross_field = self.__try_to_get_unoccupied_field_by_number(num)
                    if cross_field:
                        return cross_field

    def __try_to_get_unoccupied_field_by_number(self, field_number):
        field = self.__fields[field_number-1]
        if field.get_symbol().isdecimal():
            return field

    def __check_if_opponent_attacked_opposite_corners(self):
        to_compare_combination = [self.__opponent_symbol, self.__opponent_symbol]
        opposite_corner_fields_numbers = [(1, 9), (3, 7)]
        for nums in opposite_corner_fields_numbers:
            corner_fields = [self.__fields[nums[0]-1].get_symbol(), self.__fields[nums[1]-1].get_symbol()]
            if corner_fields == to_compare_combination:
                return True
        return False

    def __check_if_player_moving_first(self):
        if self.__check_if_is_initial_round():
            return len(self.__get_free_fields()) > 8
        return False

    def __check_if_is_initial_round(self):
        free_fields = self.__get_free_fields()
        accaptable_free_field_quantity = 8
        if len(free_fields) >= accaptable_free_field_quantity:
            return True
        return False

    def __check_if_is_second_round(self):
        free_fields = self.__get_free_fields()
        accaptable_free_field_quantity = 6
        if len(free_fields) >= accaptable_free_field_quantity:
            return True
        return False
