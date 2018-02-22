from .view import View
from tool.dataTools import DataTools


class PlayerView(View):

    def get_field_number_to_shoot(self, correct_choices):
        is_ready = False
        question = "enter field number to shoot: "
        while not is_ready:
            user_input = input(self.empty_lines + self.double_tab + question)
            if DataTools.check_if_element_in_collection(user_input, correct_choices):
                return user_input
            else:
                self.display_message("incorrect choice, try again..")
