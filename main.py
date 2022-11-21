import os
import config

from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager

from kivy.lang import Builder
from kivy.properties import StringProperty

# main screens
from screens.index import IndexScreen
from screens.login import LoginScreen
from screens.add import AddScreen
from screens.saled import SaledScreen
from screens.devolution import DevolutionScreen
from screens.request import RequestScreen
from screens.inventory import InventoryScreen
from screens.configuration import ConfigurationScreen
from screens.notification import NotificationScreen

# subs screens 
from screens.subscreens.add_produto import AddProdutoScreen


class KdemApp(MDApp):

    username = StringProperty(None)
    password = StringProperty(None)

    def __init__(self, login, **kwargs):
        super().__init__(**kwargs)
        self.__version__ = "0.2.6.3"
        self.login = login
        self.manager = ScreenManager()

    def build(self):

        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"

        Builder.load_file("kvs/login.kv")
        self.manager.add_widget(LoginScreen(self, name="login"))

        Builder.load_file("kvs/index.kv")
        self.manager.add_widget(IndexScreen(name="index"))

        Builder.load_file("kvs/add.kv")
        self.manager.add_widget(AddScreen(name="add"))

        Builder.load_file("kvs/saled.kv")
        self.manager.add_widget(SaledScreen(name="saled"))

        Builder.load_file("kvs/devolution.kv")
        self.manager.add_widget(DevolutionScreen(name="devolution"))

        Builder.load_file("kvs/request.kv")
        self.manager.add_widget(RequestScreen(name="request"))

        Builder.load_file("kvs/inventory.kv")
        self.manager.add_widget(InventoryScreen(name="inventory"))

        Builder.load_file("kvs/notification.kv")
        self.manager.add_widget(NotificationScreen(name="notification"))

        Builder.load_file("kvs/configuration.kv")
        self.manager.add_widget(ConfigurationScreen(name="configuration"))

        # ------------------------------------------------------------------------

        Builder.load_file("kvs/subkvs/add_produto.kv")
        self.manager.add_widget(AddProdutoScreen(name="add_produto"))

        return self.manager

    def get_application_config(self):
        if(not self.username):
            return super(KdemApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username

        if(not os.path.exists(conf_directory)):
            os.makedirs(conf_directory)

        return super(KdemApp, self).get_application_config(
            '%s/config.cfg' % (conf_directory)
        )


if __name__ == '__main__':

    if os.path.exists("data/account.json"):
        os.remove('data/account.json')

    KdemApp(
        login=config.data["login"]["ACCOUNTS"]
    ).run()
