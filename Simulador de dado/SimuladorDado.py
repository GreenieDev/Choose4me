#  Simulador de Dado
#  Simular a funcionalidade de um dado (valor aleatório entre 1 e 6)

import random
import PySimpleGUI as sg

class Dado:
    def __init__(self):
        #  template
        self.template = [
            [sg.Text("Atirar o dado?")],
            [sg.Button("Sim"), sg.Button("Não")],
            [sg.Output(size=(18,10))]
        ]

        # Variáveis para o range do dado
        self.valorMinimo = 1
        self.valorMáximo = 6
    
    def iniciar(self):
        #  janela
        window = sg.Window("Simulador de dado", self.template)

        #  Ler os valores da tela
        while True:
            self.event, self.values = window.Read()
            res = self.event
            try:
                if self.event == sg.WIN_CLOSED:
                    break
                if res.lower() == "sim" or res.lower() == "s":
                    print(self.rodar())
                elif res.lower() == "não" or res.lower() == "n":
                    print("Obrigado por usar o simulador de dado :)")
                    window.Close()
                
            except:
                print("Aconteceu um erro da nossa parte, sua incompetência")
        window.Close()
    
    def rodar(self):
        return random.randint(self.valorMinimo, self.valorMáximo)


dado1 = Dado()

dado1.iniciar()