import json

from kivy.app import App
from kivymd.uix.screen import MDScreen


class AddProdutoScreen(MDScreen):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = App.get_running_app().user_data_dir + '/'
        self.products_list = list()

    def on_pre_enter(self, *args):
        self.loadData()
        self.ids.retorno.text = "Novo Produto"
        self.clear_fields()

    def convert_currency(self, value):
        a = '{:,.2f}'.format(float(value))
        b = a.replace(',','v')
        c = b.replace('.',',')
        return c.replace('v','.')

    def saveData(self, *args):
        with open(self.path + 'products.json', 'w') as data_products:
            json.dump(self.products_list, data_products)

    def loadData(self, *args):
        try:
            with open(self.path + 'products.json', 'r') as data_products:
                self.products_list = json.load(data_products)
        except FileNotFoundError:
            pass

    def add_before(self, data):
        if len(self.products_list) > 0:
            for i in self.products_list:
                if i['codigo'] == data['codigo']:
                    return 'Produto existente'
        self.products_list.append(data)
        self.saveData()
        return 'Produto cadastrado'

    def backScreen(self):
        App.get_running_app().manager.current = 'add'
        App.get_running_app().manager.get_screen('add')

    def backHome(self):
        App.get_running_app().manager.current = 'index'
        App.get_running_app().manager.get_screen('index')

    def clear_fields(self):
        self.ids.codigo.text = ''
        self.ids.barcode.text = ''
        self.ids.descricao.text = ''
        self.ids.venda.text = ''
        self.ids.custo.text = ''
        self.ids.observacao.text = ''

    def produto(self, codigo, barcode, descricao, venda, custo, observacao):

        if len(codigo) == 0:
            codigo = len(self.products_list) + 1

        if len(barcode) == 0:
            barcode = 0

        if len(custo) == 0:
            custo = 0.0

        if len(observacao) == 0:
            observacao = 'Sem Observação'

        try:

            if int(venda) > 0 and len(descricao) > 0:
                if int(codigo) > 0:
                    
                    data = {
                        "codigo": int(codigo),
                        "barcode": int(barcode),
                        "descricao": descricao,
                        "venda": self.convert_currency(venda),
                        "custo": self.convert_currency(custo),
                        "observacao": observacao
                    }  

                    self.clear_fields()
                    msg = self.add_before(data)
                    self.ids.retorno.text = msg

        except ValueError:
            pass
