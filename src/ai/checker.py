from abc import ABC, abstractmethod


class Checker(ABC):

    def check_if_won(self, player_symbol):
        _board = [str(field) for field in self.board.get_fields()]
        print(_board)
        _win_combination = [player_symbol, player_symbol, player_symbol]
        sublist_len = 3
        _to_check = [_board[x:x+sublist_len] for x in (0, 3, 6)]
        _to_check += [
                    [_board[x-1] for x in (1, 4, 7)],
                    [_board[x-1] for x in (2, 5, 8)],
                    [_board[x-1] for x in (3, 6, 9)],
                    [_board[x-1] for x in (1, 5, 9)],
                    [_board[x-1] for x in (3, 5, 6)]]

        for combination in _to_check:
            if combination == _win_combination:
                return True

        return False

    def check_if_is_any_free_field(self):

        _board = [str(field) for field in self.board.get_fields()]
        for field in _board:
            if field.isdigit():
                return True

        return False
