from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window


class MainApp(App):


    def build(self):
        Window.size = (370, 390) #Tamanho inicial do executavel
        Window.set_icon('C:\\Users\\maria\Desktop\\projeto-calculadora\\media\\icon\\icon_calculadora.png')
        self.title = 'Calculadora' 
        self.operators = {"+", "-", "*", "/", "%"}  # Defina os operadores aqui
        self.last_was_operator = None 
        Window.size = (370, 370) #Tamanho inicial do executavel

        main_layout = BoxLayout(orientation='vertical') #criando o Layout Principal 

        #ORIENTAÇÕES DA CAIXA DE TEXTO
        self.caixatexto = TextInput(
            multiline=False,  #apenas uma linha
            readonly=True, #
            halign='right', #texto a direita
            size_hint=(1, 0.30), #altura do widget
            font_size=40, #tamanho do texto
            background_color=(0.7, 0.7, 0.7, 1) #cor da caixa, cinza claro
        ) 
        main_layout.add_widget(self.caixatexto) #adicionando a caixa de texto ao layout

        #######################################################################################

        #Definindo a estrutura de botões 
        button_layout = GridLayout(cols=5) # Criando layout de botões em colunas (cols)

        #Lista de botões
        referButtons = [ 
            "7", "8", "9", "/", "Clear",
            "4", "5", "6", "-", "%",
            "1", "2", "3", "*", "+"
        ]

        #Loop para criar os botões
        for i in referButtons: 
            button = Button(text=f'{i}', background_color=(0.3, 0.3, 0.3, 1)) #criando botão, adicionando texto e cor
            button.bind(on_press=self.botao_pressionado) #adicionando o manipulador de eventos
            button_layout.add_widget(button) #adicionando o botão ao layout de botões
        main_layout.add_widget(button_layout) #adicionando o layout de botões ao layout principal

        button_layout2 = GridLayout(cols=2) # Criando Novo Layout botões para "=" e "0"
        button_layout2.size_hint = (1, 0.2) # Alterando o tamanho do layout

        button0 = Button(text='0', background_color=(0.3, 0.3, 0.3, 1)) # Criando o botão "0", adicionando texto e cor
        button0.bind(on_press=self.botao_pressionado) # Adicionando o manipulador de eventos
        button_layout2.add_widget(button0) # Inserindo o botão ao novo layout

        buttonigual = Button(text='=', background_color=(0, 0.9, 0.2, 1)) # Criando o botão "=", adicionando texto e cor
        buttonigual.bind(on_press=self.calcular) # Adicionando o manipulador de eventos
        button_layout2.add_widget(buttonigual)  # Inserindo o botão ao novo layout

        main_layout.add_widget(button_layout2) #adicionando o novo layout de botões ao layout principal

        return main_layout # Retornando ao layout principal
    
    def botao_pressionado(self, varRefer):
        current = self.caixatexto.text
        button_text = varRefer.text
        if button_text == "Clear":
            self.caixatexto.text = ""
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                return
            elif current == "" and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.caixatexto.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def calcular(self, varRefer):
        texto = self.caixatexto.text
        if texto:
            texto = str(eval(self.caixatexto.text))
            self.caixatexto.text = texto


if __name__ == "__main__":
    MainApp().run()
