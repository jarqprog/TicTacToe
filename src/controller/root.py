from model.human import Human
from model.game import Game


class Root():
    
    def __init__(self):
        self.view = None

    def run_app(self):

        player1 = Human('Amiga', 'X')
        player2 = Human('PC', 'O')

        print(player1)
        print(player2)

        game = Game(player1, player2)

        print(game)

    def main_menu(self):
        pass
