
class Player():

    def __init__(self, name):
        self.name = name
        self.symbol = "-"
        self.score = 0

    def __str__(self):
        return "{} ({})".format(self.name, self.symbol)

    def get_name(self):
        return self.name

    def set_symbol(self, symbol):
        self.symbol = symbol

    def get_symbol(self):
        return self.symbol

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score
