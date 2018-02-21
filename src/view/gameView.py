from .view import View


class GameView(View):

    # def __init__(self):
    #     super().__init__()

    def display_game(self, game):

        self.display_heading()
        print(game)
