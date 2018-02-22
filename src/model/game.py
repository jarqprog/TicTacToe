
class Game():

    def __init__(self, player_1, player_2, board):
        self.player_1 = player_1
        self.player_2 = player_2
        self.players = [player_1, player_2]
        self.board = board

    def set_players(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.players = [player_1, player_2]

    def get_players(self):
        return self.players

    def get_board(self):
        return self.board

    def __str__(self):

        to_display = str(self.board)
        for num, player in enumerate(self.players):
            to_display += str(num + 1) + '. ' + str(player) + '\n\n'

        return to_display
