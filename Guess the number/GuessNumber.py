#   Um jogo em que o jogador deve tentar acertar um número aleatório de 0 a 100

import random
import PySimpleGUI as sg

class GuessNumberGame:
    def __init__(self):
        self.template = [
            [sg.Text("O seu chute: "), sg.Input(size=(3,3), key="guess")],
            [sg.Output(size=(25, 10), key="_output_")],
            [sg.Button("Enviar"), sg.Button("Novo Número"), sg.Button("Fechar")]
        ]
        self.window = sg.Window("Number Guessing Game", self.template)
    

    def Iniciar(self):
        guessingNumber = self.GenNum()
        while True:
            event, values = self.window.Read()
            guess = values["guess"]

            if event == "Enviar":
                try:
                    guess = int(guess)
                    self.Verificador(guess, guessingNumber)                    
                except:
                    print("Digite um número seu merda!")
            elif event == "Fechar" or sg.WIN_CLOSED:
                break
            if event == "Novo Número":
                guessingNumber = self.GenNum()
                self.window.FindElement("_output_").Update("")
            
        self.window.Close()

    def GenNum(self):
        return random.randint(0,100)
    
    def Verificador(self, guess, guessingNumber):
        if guess == guessingNumber:
            print("You won!")
        elif guess > guessingNumber:
            print(f"Try going smaller! ({guess})")
        elif guess < guessingNumber:
            print(f"Try going bigger! ({guess})")

jogo = GuessNumberGame()
jogo.Iniciar()