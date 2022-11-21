import os

from kaki.app import App
from kivymd.app import MDApp
from kivy.factory import Factory


class LiveApp(MDApp, App):

    DEBUG = 1

    KV_FILES = {
        os.path.join(os.getcwd(), "dev/manager/screenmanager.kv"),
        os.path.join(os.getcwd(), "dev/manager/add_produto.kv"),
    }

    CLASSES = {
        "MainScreenManager": "dev.manager.screenmanager",
        "AddProdutoScreen": "dev.manager.add_produto",
    }

    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]

    def build_app(self):

        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"

        return Factory.MainScreenManager()


if __name__ == "__main__":
    LiveApp().run()
