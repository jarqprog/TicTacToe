from model.game import Game
from view.gameView import GameView
from model.human import Human


class GameCtrl():

    def __init__(self):
        self.game = None
        self.setup_game()
        self.player_1 = self.game.get_players()[0]
        self.player_2 = self.game.get_players()[1]
        self.board = self.game.get_board()
        self.view = GameView()

    def setup_game(self):

        # to implement...

        player1 = Human('Amiga', 'X')
        player2 = Human('PC', 'O')
        self.game = Game(player1, player2)

    def execute_game_loop(self):
        
        # temporary

        self.show_game()
        self.show_board()
        self.game.get_board().change_field_to_O(1)
        self.game.get_board().change_field_to_X(9)
        self.show_game()
        self.game.get_board().change_field_to_O(2)
        self.show_game()

        self.game.get_board().change_field_to_O(2)
        winner_sign = self.get_winner_if_game_is_solved()
        self.show_game()
        print(winner_sign)

        self.game.get_board().change_field_to_O(3)
        winner_sign = self.get_winner_if_game_is_solved()
        self.show_game()
        print(winner_sign)

    def show_board(self):
        self.view.display_board(self.game.get_board())

    def show_game(self):
        self.view.display_game(self.game)

    def get_winner_if_game_is_solved(self):
        """Return winner sign or "draw" if draw or "continue" if game is not solved."""

        player_1_symbol = self.player_1.get_symbol()
        player_2_symbol = self.player_2.get_symbol()

        symbols = [player_1_symbol, player_2_symbol]
        board = sum(self.board, [])
        for symbol in symbols:
            to_compare = [symbol, symbol, symbol]
            win_horizontal = False
            win_vertical = False
            win_aslant = False
            verticals = [
                        [board[n-1] for n in (1, 4, 7)],
                        [board[n-1] for n in (2, 5, 8)],
                        [board[n-1] for n in (3, 6, 9)]]
            aslants = [
                        [board[n-1] for n in (1, 5, 9)],
                        [board[n-1] for n in (3, 5, 7)]]
            for raw in board:
                if raw == to_compare:
                    win_horizontal = True
            for raw in verticals:
                if raw == to_compare:
                    win_vertical = True
            for combi in aslants:
                if combi == to_compare:
                    win_aslant = True
            if win_horizontal or win_vertical or win_aslant:
                return symbol  # someone've won ("X" or "O")
        is_draw = True
        for square in board:
            if square.isdigit():
                is_draw = False
        if is_draw:
            return "draw"
        return "continue"
