
class ResultChecker():

    def __init__(self, board):
        self.board = board
        self.board_indexes_collection = [
                                            (1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8),
                                            (3, 6, 9), (1, 5, 9), (3, 5, 7)]

        self.board_best_indexes_collection = [
                                                (1, 2, 3), (7, 8, 9), (1, 4, 7),
                                                (3, 6, 9), (1, 5, 9), (3, 5, 7)]

    def __create_combination(self, indexes):
        fields = self.get_fields()
        return [fields[x-1] for x in indexes]

    def check_if_won(self, player_symbol):

        win_combination = [player_symbol, player_symbol, player_symbol]

        for indexes in self.board_indexes_collection:
            if win_combination == self.__create_combination(indexes):
                return True

        return False

    def check_if_is_any_free_field(self):
        for field in self.get_fields():
            if field.isdigit():
                return True

        return False

    def get_board_indexes_collection(self):
        return self.board_indexes_collection

    def get_board_best_indexes_collection(self):
        return self.board_best_indexes_collection

    def get_fields(self):
        return [str(field) for field in self.board.get_fields()]
