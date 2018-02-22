from .gameCtrl import GameCtrl


class Root():
    
    def __init__(self):
        self.view = None
        self.game_ctrl = None

    def run_app(self):
        # implementation
        # self.execute_main_menu()

        self.execute_game()

    def execute_main_menu(self):
        pass

    def execute_game(self):
        self.game_ctrl = GameCtrl()
        self.game_ctrl.execute_game_loop()

        
