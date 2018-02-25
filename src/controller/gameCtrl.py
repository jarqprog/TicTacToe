from model.game import Game
from view.gameView import GameView
from .humanCtrl import HumanCtrl
from .aiCtrl import AiCtrl
from ai.resultChecker import ResultChecker
from model.board import Board
from model.player import Player
import random


class GameCtrl():

    def __init__(self):
        self.view = GameView()
        self.board = Board()
        self.checker = ResultChecker(self.board)
        self.__setup_default_parameters()
        self.__setup_game()

    def __setup_default_parameters(self):
        self.mode = None
        self.game = None
        self.difficulty_level = None
        self.player_1_ctrl = None
        self.player_2_ctrl = None
        self.round_counter = None
        self.turn_counter = None
        self.winner = None
        self.current_player = None
        self.player_ctrls = []

    def get_board(self):
        return self.game.get_board()

    def get_player_1(self):
        return self.game.get_players()[0]

    def get_player_2(self):
        return self.game.get_players()[1]

    def __set_player_ctrls(self, player_ctrls):
        self.player_ctrls = player_ctrls

    def __setup_game(self):

        self.__execute_mode_choice()
        self.round_counter = 1
        self.turn_counter = 1

        if (self.mode == "single player"):
            self.__setup_single_player_mode()
        else:
            self.__setup_multiplayer_mode()
        self.__create_game()
        self.__generate_order_of_players()

    def execute_game_loop(self):

        should_proceed = True

        while should_proceed:
            for player in self.player_ctrls:
                self.current_player = player.get_player()
                symbol = player.get_player().get_symbol()
                self.__execute_game_screen()
                player.shoot()

                if self.checker.check_if_won(symbol):
                    self.winner = player.get_player()
                    player.increment_score()
                    self.__execute_game_screen()
                    self.__execute_win_screen()
                    should_proceed = self.__check_if_restart_game()
                    if should_proceed:
                        self.__restart_game()
                    break

                elif not self.checker.check_if_is_any_free_field():
                    self.__execute_game_screen()
                    self.__execute_draw_screen()
                    should_proceed = self.__check_if_restart_game()
                    if should_proceed:
                        self.__restart_game()
                    break

            self.turn_counter += 1

    def __execute_win_screen(self):
        self.view.animate_string("Winner is: " + str(self.winner))
        self.view.execute_pause()

    def __execute_draw_screen(self):
        self.view.animate_string("Result is draw!")
        self.view.execute_pause()

    def __execute_game_screen(self):
        player_1 = self.player_1_ctrl.get_player()
        player_2 = self.player_2_ctrl.get_player()
        self.view.clear_screen()
        self.view.display_message("Mode:    " + self.mode)
        self.view.display_message("Level:   " + self.difficulty_level)

        self.view.display_short_belt()

        self.view.display_message_in_next_line("Total score:")
        self.view.display_short_belt()
        self.view.display_message(str(player_1) + ": " + str(player_1.get_score()))
        self.view.display_message(str(player_2) + ": " + str(player_2.get_score()))
        self.view.display_message_in_next_line("Current round:    " + str(self.round_counter))
        self.view.display_message("Current turn:    " + str(self.turn_counter))
        self.view.display_message(self.current_player.get_name() + "'s moving...")
        self.view.display_message_in_next_line(str(self.board))

    def __execute_mode_choice(self):
        modes = ["single player", "multiplayer"]
        modes_index = self.view.get_game_mode(modes) - 1
        self.mode = modes[modes_index]

    def __execute_difficulty_choice(self):
        difficulties = ["easy", "normal", "hard"]
        difficulties_index = self.view.get_game_difficulty(difficulties) - 1
        self.difficulty_level = difficulties[difficulties_index]

    def __setup_single_player_mode(self):
        self.__execute_difficulty_choice()
        self.player_1_ctrl = self.__execute_player_creation()
        self.player_2_ctrl = self.__execute_ai_creation()
        self.view.animate_string("Player created! Your opponent is: " + str(self.player_2_ctrl.get_player()))
        self.view.execute_pause()

    def __setup_multiplayer_mode(self):
        self.difficulty_level = "-"
        self.player_1_ctrl = self.__execute_player_creation()
        self.view.animate_string("Player created! - " + str(self.player_1_ctrl.get_player()))
        self.player_2_ctrl = self.__execute_player_creation()
        self.view.animate_string("Player created! - " + str(self.player_2_ctrl.get_player()))
        self.view.execute_pause()

    def __create_game(self):
        self.game = Game(
                            self.player_1_ctrl.get_player(),
                            self.player_2_ctrl.get_player(),
                            self.board)

    def __generate_order_of_players(self):
        self.view.clear_screen()
        self.view.animate_string("randomly chosen movement order:")
        self.player_ctrls = [self.player_1_ctrl, self.player_2_ctrl]
        self.__set_players_symbols()
        random.shuffle(self.player_ctrls)
        __players = [
                        self.player_ctrls[0].get_player(),
                        self.player_ctrls[1].get_player()]
        self.view.display_enumerated_collection_elements(__players)

        ###

        if self.difficulty_level == "hard":
            self.player_ctrls = [
                            self.player_1_ctrl,
                            self.player_2_ctrl]

        ###
        self.view.execute_pause()

    def __set_players_symbols(self):
        self.player_ctrls[0].get_player().set_symbol("x")
        self.player_ctrls[1].get_player().set_symbol("o")

    def __execute_player_creation(self):
        name = self.view.get_name_from_user()
        return HumanCtrl(Player(name), self.board)

    def __execute_ai_creation(self):
        ai_names = ["amiga", "commodore", "atari", "zx spectrum", "schneider", "amstrad", "mikrosza"]
        name = random.choice(ai_names)
        return AiCtrl(Player(name), self.board, self.difficulty_level)

    def __check_if_restart_game(self):
        message = "Press 'r' to restart or any other key to quit game: "
        user_choice = self.view.get_text_from_user(message)
        if user_choice.lower() == "r":
            return True

        return False

    def __restart_game(self):
        self.round_counter += 1
        self.turn_counter = 0
        self.board = Board()
        self.checker = ResultChecker(self.board)
        self.player_1_ctrl.set_board(self.board)
        self.player_2_ctrl.set_board(self.board)
        self.__set_player_ctrls([self.player_1_ctrl, self.player_2_ctrl])
        self.__generate_order_of_players()
        self.__create_game()
