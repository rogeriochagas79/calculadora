from pickle import FALSE
import kivy 
from kivy.app import App
from kivy.uix.gridlayout import GridLayout 
from kivy.config import Config
from kivy.core.window import Window
import math

Window.size = (500, 700)


resultado = ''
base = '10'

class CalcGridLayout(GridLayout):
   
    def calculate(self, calculation):
       
        global resultado, base

        if base == '10':

            if calculation:

                try:
                    self.display.text = str(eval(calculation))
                    resultado = self.display.text
                except Exception:
                    self.display.text = 'Error impossível dividir por 0'
        elif base == '2':

            if calculation:

                try:

                    registrador =''
                    expressao =''
                    for x in range (len(calculation)):
                        if (calculation[x].isalnum() == True) and (x == (len(calculation)-1)):
                            registrador = registrador + calculation[x]
                            expressao += str(int(registrador,2))
                            registrador=''
                        elif calculation[x].isalnum() == True:
                            registrador = registrador + calculation[x]
                        else:
                            expressao += str(int(registrador,2)) + calculation[x]
                            registrador=''
                    resultado = expressao
                    self.display.text = f'{format(eval(expressao), "b")}'
                    resultado = str(int(self.display.text,2))

                except Exception:

                    self.display.text = 'Error impossível dividir por 0'
        
        elif base == '8':

            if calculation:

                try:

                    registrador =''
                    expressao =''
                    for x in range (len(calculation)):
                        if (calculation[x].isalnum() == True) and (x == (len(calculation)-1)):
                            registrador = registrador + calculation[x]
                            expressao += str(int(registrador,8))
                            registrador=''
                        elif calculation[x].isalnum() == True:
                            registrador = registrador + calculation[x]
                        else:
                            expressao += str(int(registrador,8)) + calculation[x]
                            registrador=''
                    resultado = expressao
                    self.display.text = f'{format(eval(expressao), "o")}'
                    resultado = str(int(self.display.text,8))

                except Exception:
                    
                    self.display.text = 'Error impossível dividir por 0'

        else:

            if calculation:

                try:

                    registrador =''
                    expressao =''
                    for x in range (len(calculation)):
                        if (calculation[x].isalnum() == True) and (x == (len(calculation)-1)):
                            registrador = registrador + calculation[x]
                            expressao += str(int(registrador,16))
                            registrador=''
                        elif calculation[x].isalnum() == True:
                            registrador = registrador + calculation[x]
                        else:
                            expressao += str(int(registrador,16)) + calculation[x]
                            registrador=''
                    resultado = expressao
                    self.display.text = f'{format(eval(expressao), "x")}'
                    resultado = str(int(self.display.text,16))

                except Exception:
                    
                    self.display.text = 'Error impossível dividir por 0'


    def binario(self, num):
            self.ids.btn_ponto.disabled = True
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
            global resultado, base
            base = '2'
            num = resultado
            try:
                self.display.text = f'{format(math.trunc(float(num)), "b")}'
            except:
                self.display.text = 'Error no se puede multiplicar entre 0'
    
    def octal(self, num):
            self.ids.btn_ponto.disabled = True
            self.ids.btn_2.disabled = False
            self.ids.btn_3.disabled = False
            self.ids.btn_4.disabled = False
            self.ids.btn_5.disabled = False
            self.ids.btn_6.disabled = False
            self.ids.btn_7.disabled = False
            self.ids.btn_8.disabled = True
            self.ids.btn_9.disabled = True
            self.ids.btn_A.disabled = True
            self.ids.btn_B.disabled = True
            self.ids.btn_C.disabled = True
            self.ids.btn_D.disabled = True
            self.ids.btn_E.disabled = True
            self.ids.btn_F.disabled = True
            global resultado, base
            base = '8'
            num = resultado
            self.display.text = f'{format(math.trunc(float(num)), "o")}'
    
    def decimal(self, num):
            self.ids.btn_ponto.disabled = False
            self.ids.btn_2.disabled = False
            self.ids.btn_3.disabled = False
            self.ids.btn_4.disabled = False
            self.ids.btn_5.disabled = False
            self.ids.btn_6.disabled = False
            self.ids.btn_7.disabled = False
            self.ids.btn_8.disabled = False
            self.ids.btn_9.disabled = False
            self.ids.btn_A.disabled = True
            self.ids.btn_B.disabled = True
            self.ids.btn_C.disabled = True
            self.ids.btn_D.disabled = True
            self.ids.btn_E.disabled = True
            self.ids.btn_F.disabled = True
            global resultado, base
            base = '10'
            num = resultado
            self.display.text = "{:.0f}".format((float(num)))
    
    def hexadecimal(self, num):
            self.ids.btn_ponto.disabled = True
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
            global resultado, base
            base = '16'
            num = resultado
            self.display.text = f'{format(math.trunc(float(num)), "x")}'
    
    def remover (self):
        self.display.text = self.display.text[:-1]
        

class CalculadoraApp(App):

    def build(self):

        return CalcGridLayout()


calcApp =CalculadoraApp()
calcApp.run()