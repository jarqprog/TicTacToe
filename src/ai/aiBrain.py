import random
from abc import ABC
from ai.resultChecker import ResultChecker


class AiBrain(ABC):
    """Parameters: player, board, checker, difficulty_level implemented in subclass - AiCtrl."""

    MIDDLE_FIELD_NUMBER = 5

    # use it to limit the availability of given procedure (method) for ai
    EASY_ACTION_FACTOR = 1
    NORMAL_ACTION_FACTOR = 10
    SMART_ACTION_FACTOR = 20
    BRILLIANT_ACTION_FACTOR = 50

    #  use it to balance ai 'intelligence' level:
    LOW_INTELLIGENCE_LVL = 30
    MEDIUM_INTELLIGENCE_LVL = 80
    HIGH_INTELLIGENCE_LVL = 180

    def __setup_parameters(self):
        self.__player_symbol = self.player.get_symbol()
        self.__opponent_symbol = self.__get_opponent_symbol()
        self.__fields = self.board.get_fields()
        self.__checker = ResultChecker(self.board)
        self.__is_player_moving_first = self.__check_if_player_moving_first()
        self.__intelligence_factor = self.__get_intelligence_factor()

    def attack_field(self):

        self.__setup_parameters()

        procedures = (
                        self.__try_to_get_field_to_win_or_block,
                        self.__try_to_get_middle_field_while_defending,
                        self.__try_to_get_field_to_block_opposite_corner_tactic,
                        self.__try_to_get_opposite_corner_field,
                        self.__try_to_get_field_from_best_combination,
                        self.__try_to_get_any_free_field)

        for procedure in procedures:
            field = procedure()
            if field:
                field.set_symbol(self.__player_symbol)
                break

    def __get_intelligence_factor(self):

        if self.difficulty_level == "easy":
            intelligence = self.LOW_INTELLIGENCE_LVL
        elif self.difficulty_level == "normal":
            intelligence = self.MEDIUM_INTELLIGENCE_LVL
        else:
            intelligence = self.HIGH_INTELLIGENCE_LVL

        return random.randint(0, intelligence)

    def __try_to_get_field_from_best_combination(self):

        if self.__intelligence_factor > self.NORMAL_ACTION_FACTOR:
            combi = self.__select_best_combination()
            if combi:
                best_fields = [field for field in (combi[0], combi[2]) if field.get_symbol().isdecimal()]  # edge fields
                if best_fields:
                    return random.choice(best_fields)
                return combi[1]  # middle field

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
                if len(combi) == 3]  # avoid lost combination where opponent has own symbol

    def __create_combination(self, indexes):
        return [self.__fields[x-1] for x in indexes
                if self.__fields[x-1].get_symbol() != self.__opponent_symbol]

    def __get_opponent_symbol(self):
        if self.__player_symbol == "x":
            return "o"
        return "x"

    def __try_to_get_any_free_field(self):
        free_fields = self.__get_free_fields()
        if free_fields:
            return random.choice(free_fields)

    def __get_free_fields(self):
        return [field for field in self.__fields if field.get_symbol().isdigit()]

    def __try_to_get_field_to_win_or_block(self):

        if self.__intelligence_factor > self.EASY_ACTION_FACTOR:
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

    def __try_to_get_opposite_corner_field(self):

        cond_0 = self.__intelligence_factor > self.SMART_ACTION_FACTOR
        cond_1 = self.__is_player_moving_first
        cond_2 = self.__check_if_it_is_given_turn(2)  # is it second turn?
        cond_3 = self.__check_if_given_field_is_unoccupied(self.MIDDLE_FIELD_NUMBER)

        if cond_0 & cond_1 & cond_2 & cond_3:
            opposite_corner_fields_pairs = {1: 9, 3: 7, 7: 3, 9: 1}
            for key, value in opposite_corner_fields_pairs.items():
                if self.__fields[key-1].get_symbol() == self.__player_symbol:
                    if self.__fields[value-1].get_symbol().isdecimal():
                        return self.__fields[value-1]

    def __try_to_get_middle_field_while_defending(self):

        cond_0 = self.__intelligence_factor > self.BRILLIANT_ACTION_FACTOR
        cond_1 = not self.__is_player_moving_first
        cond_2 = self.__check_if_it_is_given_turn(1)  # is it first turn?

        if cond_0 & cond_1 & cond_2:
            return self.__try_to_get_unoccupied_field_by_number(self.MIDDLE_FIELD_NUMBER)

    def __try_to_get_field_to_block_opposite_corner_tactic(self):

        cond_0 = self.__intelligence_factor > self.SMART_ACTION_FACTOR
        cond_1 = not self.__is_player_moving_first
        cond_2 = self.__check_if_it_is_given_turn(2)  # is it second turn?
        cond_3 = not self.__check_if_given_field_is_unoccupied(self.MIDDLE_FIELD_NUMBER)

        if cond_0 & cond_1 & cond_2 & cond_3:
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

    def __check_if_given_field_is_unoccupied(self, field_number):
        if self.__try_to_get_unoccupied_field_by_number(field_number):
            return True
        return False

    def __check_if_opponent_attacked_opposite_corners(self):
        to_compare_combination = [self.__opponent_symbol, self.__opponent_symbol]
        opposite_corner_fields_numbers = [(1, 9), (3, 7)]
        for nums in opposite_corner_fields_numbers:
            corner_fields = [self.__fields[nums[0]-1].get_symbol(), self.__fields[nums[1]-1].get_symbol()]
            if corner_fields == to_compare_combination:
                return True
        return False

    def __check_if_player_moving_first(self):
        if self.__check_if_it_is_given_turn(1):
            return len(self.__get_free_fields()) > 8
        return self.__is_player_moving_first

    def __check_if_it_is_given_turn(self, turn_number):
        max_free_fields_quantity = 9
        current_free_fields_quantity = len(self.__get_free_fields())
        min_fields_quantity = max_free_fields_quantity - ((turn_number-1) * 2) - 1
        max_fields_quantity = min_fields_quantity + 1
        return current_free_fields_quantity in (min_fields_quantity, max_fields_quantity)
