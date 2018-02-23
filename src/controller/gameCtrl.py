from model.game import Game
from view.gameView import GameView
from model.human import Human
from model.ai import Ai
from .humanCtrl import HumanCtrl
from .aiCtrl import AiCtrl
from model.board import Board
import random


class GameCtrl():

    def __init__(self):
        self.view = GameView()
        self.board = Board()
        self.__setup_default_parameters()
        self.__setup_game()

    def __setup_default_parameters(self):
        self.mode = None
        self.game = None
        self.difficulty = None
        self.player_1_ctrl = None
        self.player_2_ctrl = None
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

    def __setup_game(self):

        self.__execute_mode_choice()
        self.turn_counter = 1

        if (self.mode == "single player"):
            self.__setup_single_player_mode()
        else:
            self.__setup_multiplayer_mode()
        self.__create_game()
        self.__generate_order_of_players()

    def execute_game_loop(self):

        should_continue = True
        while should_continue:
            for player in self.player_ctrls:
                self.current_player = player.get_player()
                symbol = player.get_player().get_symbol()
                self.__execute_game_screen()
                player.shoot()
                if self.__check_if_won(symbol):
                    self.winner = player.get_player()
                    self.__execute_win_screen()
                    should_continue = False
                    break
                elif not self.__check_if_is_any_free_field():
                    self.__execute_draw_screen()
                    should_continue = False
                    break
            self.turn_counter += 1

    def __execute_win_screen(self):
        self.view.clear_screen()
        self.view.display_message_in_next_line("Winner is: " + str(self.winner))
        self.view.execute_pause()

    def __execute_draw_screen(self):
        self.view.clear_screen()
        self.view.display_message_in_next_line("Result is draw!")
        self.view.execute_pause()

    def __execute_game_screen(self):
        self.view.clear_screen()
        self.view.display_message("Mode:    " + self.mode)
        self.view.display_message("Level:   " + self.difficulty_level)
        self.view.display_message_in_next_line("Turn:    " + str(self.turn_counter))
        self.view.display_message("Player:  " + str(self.current_player))
        self.view.display_message_in_next_line(str(self.board))

    def __check_if_won(self, player_symbol):
        # player_symbol = x or o
        _board = [str(field) for field in self.board.get_fields()]
        _win_combination = [player_symbol, player_symbol, player_symbol]
        sublist_len = 3
        _to_check = [_board[x:x+sublist_len] for x in (0, 3, 6)]
        _to_check += [
                    [_board[x-1] for x in (1, 4, 7)],
                    [_board[x-1] for x in (2, 5, 8)],
                    [_board[x-1] for x in (3, 6, 9)],
                    [_board[x-1] for x in (1, 5, 9)],
                    [_board[x-1] for x in (3, 5, 6)]]

        for combination in _to_check:
            if combination == _win_combination:
                return True

        return False

    def __check_if_is_any_free_field(self):

        _board = [str(field) for field in self.board.get_fields()]
        for field in _board:
            if field.isdigit():
                return True
        return False

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
        self.view.display_message_in_next_line(
                                                "Player created! Your opponent is: " +
                                                str(self.player_2_ctrl.get_player()))
        self.view.execute_pause()

    def __setup_multiplayer_mode(self):
        self.difficulty_level = "-"
        self.player_1_ctrl = self.__execute_player_creation()
        self.view.display_message_in_next_line("Player created!")
        self.player_2_ctrl = self.__execute_player_creation()
        self.view.display_message_in_next_line("Player created!")

    def __create_game(self):
        self.game = Game(
                            self.player_1_ctrl.get_player(),
                            self.player_2_ctrl.get_player(),
                            self.board)

    def __generate_order_of_players(self):
        self.view.clear_screen()
        self.view.display_message("drew the order of players:")
        self.player_ctrls = [self.player_1_ctrl, self.player_2_ctrl]
        self.__set_players_symbols()
        random.shuffle(self.player_ctrls)
        __players = [
                        self.player_ctrls[0].get_player(),
                        self.player_ctrls[1].get_player()]
        self.view.display_enumerated_collection_elements(__players)
        self.view.execute_pause()

    def __set_players_symbols(self):
        self.player_ctrls[0].get_player().set_symbol("x")
        self.player_ctrls[1].get_player().set_symbol("o")

    def __execute_player_creation(self):
        name = self.view.get_name_from_user()
        return HumanCtrl(Human(name), self.board)

    def __execute_ai_creation(self):
        ai_names = ["amiga", "commodore", "atari", "zx spectrum", "schneider", "amstrad", "mikrosza"]
        name = random.choice(ai_names)
        return AiCtrl(Ai(name), self.board)
