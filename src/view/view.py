import time
import sys
import os

from tool.dataTools import DataTools


class View():

    # import getch (avoid problem with windows/ubuntu):
    try:
        from msvcrt import getwch as getch

    except ImportError:
        @staticmethod
        def getch():
            import tty
            import termios
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

    def __init__(self):
        self.empty_lines = "\n\n"
        self.double_tab = "\t\t"
        self.long_heading_multiplier = 93
        self.short_heading_multiplier = 40
        self.title = "tic tac toe"
        self.long_heading = "#"*self.long_heading_multiplier
        self.short_heading = "#"*self.short_heading_multiplier

    def display_heading(self):
        print(self.long_heading)
        print("{} {} {}".format(self.short_heading, self.title, self.short_heading))
        print(self.long_heading)

    def display_message(self, message):
        print(self.double_tab + message)

    def display_message_in_next_line(self, message):
        print(self.empty_lines + self.double_tab + message)

    def display_empty_lines(self):
        print(self.empty_lines)

    def display_short_belt(self):
        belt = "-" * self.short_heading_multiplier
        print(self.double_tab + belt)

    def get_text_from_user(self, message):
        should_continue = True
        print(self.empty_lines)
        while should_continue:
            user_input = input(self.double_tab + message)
            if user_input:
                should_continue = False
        return user_input

    def animate_string(self, text, latency=0.1):
        """
        Display string using pseudo-animating technique.

        speed: determine "animating" speed (float), default: 0.0005
        string: string text to display
        """
        text = self.empty_lines + self.double_tab + text
        for char in text:
            sys.stdout.write("%s" % char)
            sys.stdout.flush()
            time.sleep(latency)
            latency = latency * 0.9

    def clear_screen(self):
        """Clear screen - universal for ubuntu/windows platform."""
        os.system('cls' if os.name == 'nt' else 'clear')
        self.display_heading()
        self.display_empty_lines()

    def execute_pause(self):
        """Stop program action until user will press any key."""
        print(self.empty_lines + self.double_tab + "to continue press any key..\r")
        self.getch()

    def display_enumerated_collection_elements(self, collection):
        self.display_empty_lines()
        for num, element in enumerate(collection):
            to_display = "{}[{}]: {}".format(self.double_tab, num+1, element)
            print(to_display)
        self.display_empty_lines()

    def get_user_choice_from_enumerated_collection(self, collection, message):
        """Return integer number."""
        correct_choices = [str(x+1) for x in range(len(collection))]
        is_choice_ready = False
        while not is_choice_ready:
            self.clear_screen()
            self.animate_string(message)
            self.display_enumerated_collection_elements(collection)
            user_choice = input(self.double_tab)
            if DataTools.check_if_element_in_collection(user_choice, correct_choices):
                is_choice_ready = True
        return int(user_choice)

    def display_text_with_asci_graphics(self, text, repeat=9):
        """
        Display text and asci graphisc in pseudo-animating form.

        Parameters:
        text: string (text to display)
        repeat: integer (number of repeats in loop)

        Sample output:
        ***************************2....
        *****************************1..
        *******************************0
        text
        """

        for counter in range(repeat, -1, -1):
            stars = "\r\r{: >25}".format("ox"*counter)
            self.animate_string(stars, latency=0.005)
        self.animate_string(self.double_tab + text)
        self.display_empty_lines()
