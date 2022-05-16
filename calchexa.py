from re import T
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.app import App

Window.size = (500, 700)

Builder.load_file('calch.kv')


class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'

    def button_press(self, button):
        prior = self.ids.calc_input.text

        if "Erro" in prior:
            prior = ''

        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    def remove(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        self.ids.calc_input.text = prior

    def pos_neg(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{prior}'

    def dot(self):
        prior = self.ids.calc_input.text
        num_list = prior.split("+")

        if "+" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = f'{prior}'

        elif "." in prior:
            pass
        else:
            prior = f'{prior}.'
            self.ids.calc_input.text = f'{prior}'

    def add(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}+'

    def multiply(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}*'

    def subtract(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}-'

    def divide(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}/'

    def bin(self):
        prior = self.ids.calc_input.text
        self.ids.btn_2.disabled = True
        self.ids.btn_3.disabled = True
        self.ids.btn_4.disabled = True
        self.ids.btn_5.disabled = True
        self.ids.btn_6.disabled = True
        self.ids.btn_7.disabled = True
        self.ids.btn_8.disabled = True
        self.ids.btn_9.disabled = True
        self.ids.btn_A.disabled = True
        self.ids.btn_B.disabled = True
        self.ids.btn_C.disabled = True
        self.ids.btn_D.disabled = True
        self.ids.btn_E.disabled = True
        self.ids.btn_F.disabled = True
        try:
            entrada = eval(prior)
            entrada = int(entrada)
            self.ids.calc_input.text = f'{format(entrada, "b")}'
        except:
            self.ids.calc_input.text = "Erro"

    def hex(self):
        prior = self.ids.calc_input.text
        self.ids.btn_2.disabled = False
        self.ids.btn_3.disabled = False
        self.ids.btn_4.disabled = False
        self.ids.btn_5.disabled = False
        self.ids.btn_6.disabled = False
        self.ids.btn_7.disabled = False
        self.ids.btn_8.disabled = False
        self.ids.btn_9.disabled = False
        self.ids.btn_A.disabled = False
        self.ids.btn_B.disabled = False
        self.ids.btn_C.disabled = False
        self.ids.btn_D.disabled = False
        self.ids.btn_E.disabled = False
        self.ids.btn_F.disabled = False
        try:
            entrada = eval(prior)
            entrada = int(entrada)
            self.ids.calc_input.text = f'{format(entrada, "x")}'
        except:
            self.ids.calc_input.text = "Erro"

    def oct(self):
        prior = self.ids.calc_input.text
        self.ids.btn_2.disabled = False
        self.ids.btn_3.disabled = False
        self.ids.btn_4.disabled = False
        self.ids.btn_5.disabled = False
        self.ids.btn_6.disabled = False
        self.ids.btn_7.disabled = True
        self.ids.btn_8.disabled = True
        self.ids.btn_9.disabled = True
        self.ids.btn_A.disabled = True
        self.ids.btn_B.disabled = True
        self.ids.btn_C.disabled = True
        self.ids.btn_D.disabled = True
        self.ids.btn_E.disabled = True
        self.ids.btn_F.disabled = True
        try:
            entrada = eval(prior)
            entrada = int(entrada)
            self.ids.calc_input.text = f'{format(entrada, "o")}'
        except:
            self.ids.calc_input.text = "Erro"

    def equals(self):
        prior = self.ids.calc_input.text
        try:
            answer = eval(prior)
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "Erro"

    """ if "+" in prior:
            num_list = prior.split("+")
            answer = 0.0
            for number in num_list:
                answer = answer + float(number)

            self.ids.calc_input.text = str(answer)
        """


class CalculadoraApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    CalculadoraApp().run()
