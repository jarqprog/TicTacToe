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
        self.view.display_game(self.game)
