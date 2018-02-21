import time
import sys
import os


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

    @staticmethod
    def animate_string(speed=0.0005, string=None):
        """
        Display string using pseudo-animating technique.

        speed: determine "animating" speed (float), default: 0.0005
        string: string text to display
        """
        if string is None:
            string = "\n\nLoading program...\n\n"
        for char in string:
            sys.stdout.write("%s" % char)
            sys.stdout.flush()
            time.sleep(speed)

    @staticmethod
    def clear_screen():
        """Clear screen - universal for ubuntu/windows platform."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def execute_pause(self):
        """Stop program action until user will press any key."""
        print(self.empty_lines + self.double_tab + "to continue press any key.." + self.empty_lines)
        self.getch()

