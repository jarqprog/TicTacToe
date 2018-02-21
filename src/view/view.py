
class View():
    
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

