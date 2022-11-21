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

    def add(self, data):
        if len(self.products_list) > 0:
            for i in self.products_list:
                if i['code'] == data['code']:
                    return 'Produto existente'
        self.products_list.append(data)
        self.saveData()
        return 'Produto cadastrado'

    def back(self):
        self.manager.current = 'add'
        self.manager.get_screen('add')

    def clear_fields(self):
        self.ids.codigo.text = ''
        self.ids.barcode.text = ''
        self.ids.descricao.text = ''
        self.ids.venda.text = ''
        self.ids.custo.text = ''
        self.ids.observacao.text = ''

    def produto(self, codigo, barcode, descricao, venda, custo, observacao):

        self.clear_fields()

        if len(codigo) == 0:
            codigo = 0

        if len(barcode) == 0:
            barcode = 0

        if len(venda) == 0:
            venda = 0.0

        if len(custo) == 0:
            custo = 0.0

        if len(descricao) == 0:
            descricao = 'Sem descrição'

        if len(observacao) == 0:
            observacao = 'Sem Observação'

        data = {
            "codigo": int(codigo),
            "barcode": int(barcode),
            "descricao": descricao,
            "venda": self.convert_currency(venda),
            "custo": self.convert_currency(custo),
            "observacao": observacao
        }

        msg = self.add(data)
        self.ids.retorno.text = msg

    