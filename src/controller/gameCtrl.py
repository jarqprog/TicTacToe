from model.game import Game
from view.gameView import GameView
from model.human import Human
from .humanCtrl import HumanCtrl
from model.board import Board


class GameCtrl():

    def __init__(self):
        self.game = None
        self.player_1_ctrl = None
        self.player_2_ctrl = None
        self.turn_counter = None
        self.winner = None
        self.current_player = None
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
        board = Board()

        player_1 = Human('Rob', 'x')
        self.player_1_ctrl = HumanCtrl(player_1, board)

        player_2 = Human('Alex', 'o')
        self.player_2_ctrl = HumanCtrl(player_2, board)

        self.game = Game(player_1, player_2, board)
        self.turn_counter = 1

    def execute_game_loop(self):

        players = [self.player_1_ctrl, self.player_2_ctrl]
        should_continue = True
        while should_continue:
            for player in players:
                self.current_player = player.get_player()
                symbol = player.get_player().get_symbol()
                self.execute_game_screen()
                player.shoot()
                if self.check_if_won(symbol):
                    self.winner = player.get_player()
                    self.execute_win_screen()
                    should_continue = False
                    break
                elif not self.check_if_is_any_free_field():
                    self.execute_draw_screen()
                    should_continue = False
                    break
            self.turn_counter += 1

    def execute_win_screen(self):
        self.view.clear_screen()
        self.view.display_message("Winner is: " + str(self.winner))
        self.view.execute_pause()

    def execute_draw_screen(self):
        self.view.clear_screen()
        self.view.display_message("Result is draw!")
        self.view.execute_pause()

    def show_board(self):
        self.view.display_board(self.game.get_board())

    def execute_game_screen(self):
        self.view.clear_screen()
        self.view.display_board(str(self.game.get_board()))
        self.view.display_message("Turn: " + str(self.turn_counter))
        self.view.display_message("Player: " + str(self.current_player))

    def check_if_won(self, player_symbol):
        # player_symbol = x or o
        _board = [str(field) for field in self.game.get_board().get_fields()]
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

        _board = [str(field) for field in self.game.get_board().get_fields()]
        for field in _board:
            if field.isdigit():
                return True
        return False
