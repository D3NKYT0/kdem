from kivymd.uix.screen import MDScreen


class AddScreen(MDScreen):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def back(self):
        self.manager.current = 'index'
        self.manager.get_screen('index')

    def produto(self):
        self.manager.current = 'add_produto'
        self.manager.get_screen('add_produto')
    