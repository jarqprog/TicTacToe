from .view import View


class GameView(View):

    # def __init__(self):
    #     super().__init__()

    def display_board(self, board):
        print(board)

    def display_game(self, game):
        self.clear_screen()
        self.display_heading()
        print(game)
        self.execute_pause()
