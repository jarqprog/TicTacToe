from .view import View


class RootView(View):

    def display_intro(self):
        text = "*** welcome to TIC TAC TOE by jq ***"
        self.clear_screen()
        self.display_text_with_asci_graphics(text)
        self.execute_pause()
