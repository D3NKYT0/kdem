import json

from kivymd.uix.screen import MDScreen


class LoginScreen(MDScreen):
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        self.__version__ = "Version: " + self.app.__version__

        self.ids.toolbar.title = self.__version__ 
        self.login = self.app.login

        self.ids.email_field.text = "admin@admin.com"
        self.ids.password_field.text = "admin"

    def data_callback(self):
        pass

    def check_callback(self):
        self.app.stop()

    def enter(self, email, password):

        # ------------ fazer verificação -------------
        if len(email) > 0 and len(password) > 0:
            self.do_login(email, password)
        # --------------------------------------------

    def do_login(self, loginText, passwordText):
        
        if loginText.lower() in self.login.keys():
            if passwordText == self.login[loginText.lower()]:

                data_acc = {
                    "email": loginText,
                    "user": "Admin" 
                }

                with open('data/account.json', 'w') as account:
                    json.dump(data_acc, account)

                self.app.username = loginText
                self.app.password = passwordText

                self.manager.current = 'index'
                self.manager.get_screen('index')

                self.app.config.read(self.app.get_application_config())
                self.app.config.write()
