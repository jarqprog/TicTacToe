from .checker import Checker


class ResultChecker(Checker):

    def __init__(self, board):
        super().__init__()
        self.board = board
