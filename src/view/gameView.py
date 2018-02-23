from .view import View


class GameView(View):

    def get_game_mode(self, modes):
        message = "Select game mode:"
        return self.get_user_choice_from_enumerated_collection(modes, message)

    def get_game_difficulty(self, difficulties):
        message = "Select game difficulty level:"
        return self.get_user_choice_from_enumerated_collection(difficulties, message)

    def get_name_from_user(self):
        return self.get_text_from_user("Please, enter Your name: ").capitalize()
