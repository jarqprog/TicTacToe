from model.game import Game
from view.gameView import GameView
from model.human import Human


class GameCtrl():

    def __init__(self):
        self.game = None
        self.setup_game()
        self.view = GameView()

    def get_board(self):
        return self.game.get_board()

    def get_player_1(self):
        return self.game.get_players()[0]

    def get_player_2(self):
        return self.game.get_players()[1]

    def setup_game(self):

        # to implement...

        player1 = Human('Amiga', 'X')
        player2 = Human('PC', 'O')
        self.game = Game(player1, player2)

    def execute_game_loop(self):

        # temporary


        #####################

        self.show_board()
        self.game.get_board().change_field_to_X(1)
        has_won = self.check_if_won(self.get_player_1().get_symbol())
        print(str(has_won))

        self.show_board()
        self.game.get_board().change_field_to_X(2)
        has_won = self.check_if_won(self.get_player_1().get_symbol())
        print(str(has_won))

        self.show_board()
        self.game.get_board().change_field_to_X(4)
        has_won = self.check_if_won(self.get_player_1().get_symbol())
        print(str(has_won))

        self.show_board()
        self.game.get_board().change_field_to_X(3)
        has_won = self.check_if_won(self.get_player_1().get_symbol())
        print(str(has_won))

        # prinet

        self.show_board()

        self.game.get_board().change_field_to_X(5)
        self.game.get_board().change_field_to_X(6)
        self.game.get_board().change_field_to_X(7)
        is_draw = self.check_if_is_any_free_field()
        print("is free field::", str(is_draw))
        self.game.get_board().change_field_to_X(8)
        is_draw = self.check_if_is_any_free_field()
        print("is free field::", str(is_draw))
        self.show_board()
        self.game.get_board().change_field_to_X(9)
        is_draw = self.check_if_is_any_free_field()
        self.show_board()
        print("is free field:", str(is_draw))

        #####################

    def show_board(self):
        self.view.display_board(self.game.get_board())

    def show_game(self):
        self.view.display_game(self.game)

    def check_if_won(self, player_symbol):
        # player_symbol = x or o
        _board = [str(field) for field in self.game.get_board().get_fields()]
        print("fields: ", _board)
        _win_combination = [player_symbol, player_symbol, player_symbol]
        print(player_symbol)
        self.view.execute_pause()
        sublist_len = 3
        _to_check = [_board[x:x+sublist_len] for x in (0, 3, 6)]
        _to_check += [
                    [_board[x-1] for x in (1, 4, 7)],
                    [_board[x-1] for x in (2, 5, 8)],
                    [_board[x-1] for x in (3, 6, 9)],
                    [_board[x-1] for x in (1, 5, 9)],
                    [_board[x-1] for x in (3, 5, 6)]]

        for lista in _to_check:
            print(str(lista))

        for combination in _to_check:
            print(combination, "bool ", str(combination == _win_combination))
            if combination == _win_combination:
                return True

        return False

    def check_if_is_any_free_field(self):

        _board = [str(field) for field in self.game.get_board().get_fields()]
        for field in _board:
            if field.isdigit():
                return True
        return False
