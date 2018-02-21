from model.game import Game
from view.gameView import GameView
from model.human import Human


class GameCtrl():

    def __init__(self):
        self.game = None
        self.setup_game()
        self.view = GameView()

    def setup_game(self):

        player1 = Human('Amiga', 'X')
        player2 = Human('PC', 'O')
        self.game = Game(player1, player2)

    def execute_game_loop(self):
        self.show_game()
        self.show_board()
        self.game.get_board().change_field_to_O(1)
        self.game.get_board().change_field_to_X(9)
        self.show_game()
        self.game.get_board().change_field_to_O(2)
        self.show_game()

    def show_board(self):
        self.view.display_board(self.game.get_board())

    def show_game(self):
        self.view.display_game(self.game)
