from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout

from kivy.app import App
from kivy.properties import ObjectProperty

import json

import sys
sys.path.insert(1, './config')

import config

from custom.widgets import *


class Content(MDBoxLayout):

    # variaveis de classe
    nav_drawer = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load_account(self):

        try:
            with open('data/account.json', 'r') as account:
                data_account = json.load(account)
        except FileNotFoundError:
            data_account = {"user": "KDEM", "email": "suporte@kdem.br"}

        self.ids.user_name.text = data_account['user']
        self.ids.user_email.text = data_account['email']

    def logout(self):
        App.get_running_app().manager.current = 'login'
        App.get_running_app().manager.get_screen('login')

    def add(self):
        App.get_running_app().manager.current = 'add'
        App.get_running_app().manager.get_screen('add')

    def saled(self):
        App.get_running_app().manager.current = 'saled'
        App.get_running_app().manager.get_screen('saled')

    def request(self):
        App.get_running_app().manager.current = 'request'
        App.get_running_app().manager.get_screen('request')

    def devolution(self):
        App.get_running_app().manager.current = 'devolution'
        App.get_running_app().manager.get_screen('devolution')

    def inventory(self):
        App.get_running_app().manager.current = 'inventory'
        App.get_running_app().manager.get_screen('inventory')


class IndexScreen(MDScreen):

    # variaveis de classe
    content = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ids.nav_drawer.set_state("close")

        self.ids.announce.text = config.data["announce"]["today"]
        self.clock = ClockRealTime(widget=self).start()

    def on_pre_enter(self):
        self.ids.data.text = str(self.clock.date)
        self.ids.hora.text = str(self.clock.hour)

    def open_menu(self):
        self.ids.content.load_account()
        self.ids.nav_drawer.set_state("open")

    def saled(self):
        self.ids.nav_drawer.set_state("close")
        App.get_running_app().manager.current = 'saled'
        App.get_running_app().manager.get_screen('saled')

    def request(self):
        self.ids.nav_drawer.set_state("close")
        App.get_running_app().manager.current = 'request'
        App.get_running_app().manager.get_screen('request')

    def notification(self):
        self.ids.nav_drawer.set_state("close")
        App.get_running_app().manager.current = 'notification'
        App.get_running_app().manager.get_screen('notification')

    def configuration(self):
        self.ids.nav_drawer.set_state("close")
        App.get_running_app().manager.current = 'configuration'
        App.get_running_app().manager.get_screen('configuration')
