from kivymd.uix.screen import MDScreen


class SaledScreen(MDScreen):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def back(self):
        self.manager.current = 'index'
        self.manager.get_screen('index')
