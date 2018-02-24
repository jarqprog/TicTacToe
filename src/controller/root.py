from .gameCtrl import GameCtrl
from view.rootView import RootView


class Root():

    def __init__(self):
        self.view = RootView()
        self.game_ctrl = None

    def run_app(self):
        self.view.display_intro()
        self.execute_game()

    def execute_main_menu(self):
        pass

    def execute_game(self):
        self.game_ctrl = GameCtrl()
        self.game_ctrl.execute_game_loop()
