import random
import PySimpleGUI as sg

class choose4me:
    def __init__(self):
        self.Respostas = [
            #Frases positivas
            "Na minha opinião, acho que sim!",
            "Sim!!!",
            "Óbvio!",

            #Frases negativas
            "Não!!",
            "Eu acho que isso não é uma boa deia...",
            "Podes tentar, mas acho que o tiro vai sair pela colatra.",

            #Frases neutras
            "Honestamente, eu não sei...",
            "Acho que não precisas de mim para tomar essa decisão, segue o teu coração!",
            "Não sei o que te dizer..."

        ]
        self.template = [
            [sg.Text("O que lhe atormenta a mente?")],
            [sg.Input(), sg.Button("Enviar") ],
            [sg.Output(key="_output_",size=(50,10))],
            [sg.Button("Limpar"),sg.Button("Sair")]
        ]

    def Iniciar(self):
        window = sg.Window("Assistente de Decisões", self.template)
        while True:
            event, values = window.Read()
            if event == "Sair" or event == sg.WIN_CLOSED:
                break
            elif event == "Enviar":
                print(f"[Choose4me]: {self.Decidir()}")
            elif event == "Limpar":
                window.FindElement("_output_").Update("")
        window.Close() 
    
    def Decidir(self):
        res = random.randint(0, len(self.Respostas) - 1)
        return self.Respostas[res]



EscolhaBot = choose4me()
EscolhaBot.Iniciar()