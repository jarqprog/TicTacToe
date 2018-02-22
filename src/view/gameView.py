from .view import View


class GameView(View):

    def display_board(self, board):
        self.display_message("Game board:")
        self.display_message(board)
