from .gameCtrl import GameCtrl
from view.rootView import RootView
from manager.fileManager import FileManager


class Root():

    INTRO_FILE_PATH = "intro.txt"
    OUTRO_FILE_PATH = "outro.txt"

    def __init__(self):
        self.view = RootView()
        self.game_ctrl = None

    def run_app(self):
        self.view.maximize_console()
        self.execute_intro()
        self.execute_game()
        self.execute_outro()

    def execute_main_menu(self):
        pass  # to implement

    def execute_game(self):
        self.game_ctrl = GameCtrl()
        self.game_ctrl.execute_game_loop()

    def execute_intro(self):
        file_manager = FileManager(self.INTRO_FILE_PATH)
        collection = file_manager.import_data()
        self.view.clear_screen()
        self.view.display_collection_with_animate_strings(collection)
        self.view.execute_pause()

    def execute_outro(self):
        file_manager = FileManager(self.OUTRO_FILE_PATH)
        collection = file_manager.import_data()
        self.view.clear_screen()
        self.view.display_collection_with_animate_strings(collection)
        self.view.execute_pause()
