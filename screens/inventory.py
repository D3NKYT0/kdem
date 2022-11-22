import json

from kivy.app import App
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import ThreeLineIconListItem


class InventoryScreen(MDScreen):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = App.get_running_app().user_data_dir + '/'
        self.products_list = list()

    def on_pre_enter(self, *args):

        self.loadData()
        if len(self.products_list) == 0:
            self.ids.notification_product.text = "Nenhum produto cadastrado!"

        self.ids.lista_de_produtos.clear_widgets()

        for product in self.products_list:
            self.ids.lista_de_produtos.add_widget(Product(product, self))

    def back(self):
        self.manager.current = 'index'
        self.manager.get_screen('index')

    def search(self):
        pass

    def filter(self):
        pass

    def removeWidget(self, products):
        descricao = str(products.text).replace("Nome: ", "")
        self.ids.lista_de_produtos.remove_widget(products)
        for i in self.products_list:
            if i['descricao'] == descricao:
                self.products_list.remove(i)
                self.saveData()

    def saveData(self, *args):
        with open(self.path + 'products.json', 'w') as data_products:
            json.dump(self.products_list, data_products)

    def loadData(self, *args):
        try:
            with open(self.path + 'products.json', 'r') as data_products:
                self.products_list = json.load(data_products)
        except FileNotFoundError:
            pass


class Product(ThreeLineIconListItem):
    def __init__(self, product, inventory_callback, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = f'Nome: {product["descricao"]}'
        self.secondary_text = f'Preço: R$ {product["venda"]}'
        self.tertiary_text = f'Quantidade: Indefinido'
        self.inventory_callback = inventory_callback

    def remove(self):
        self.inventory_callback.removeWidget(self)
