import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WIN_CLOSED

class AdventureGame:
    def __init__(self):
        self.playing = True
        self.race = ""
        self.DidHelp = False
        self.defense = ""

        self.pergunta1 = "What is your race (Human or Witch):    "
        self.pergunta2 = "\nThe time has passed and now you have to choose a way of defending yourself (Karate or Fire Magic):    "
        self.pergunta3 = "\nA slime needs help to get to its slimy familly, will you help (yes or no):    "
        self.pergunta4 = "\nYou get in a battle with someone really bad, do you run or fight (run or fight):    "

        self.template = [
            [sg.Output(size=(50,10), key = "respostas")],
            [sg.Input(size=(55,0), key = "input")],
            [sg.Button("Começar"), sg.Button("Fechar")]
        ]

    
    def Iniciar(self):
        self.window = sg.Window("Adventure Game", self.template) 
        while True:
            self.LerValores()

            if self.event == sg.WIN_CLOSED or self.event == "Fechar":
                break
            else:
                #   Fase 0 - Raça
                fase = 0
                print(self.pergunta1)
                self.LerValores()
                print(self.PedirResposta(fase))

                #   Fase 1 - Método de defesa
                fase += 1
                print(self.pergunta2)
                self.LerValores()
                print(self.PedirResposta(fase))
                if self.playing == False:
                    break

                #   Fase 2 - Ajudar o slime?
                fase += 1
                print(self.pergunta3)
                self.LerValores()
                print(self.PedirResposta(fase))

                #   Fase 3 - Batalha
                fase += 1
                print(self.pergunta4)
                self.LerValores()
                print(self.PedirResposta(fase))
        sg.Close()


    def PedirResposta(self, fase):
        if fase == 0:
            self.race = self.values["input"]
            if self.race.lower() == "human":
                self.race = "Human"    
            else:
                self.race = "Witch"
            return f"A {self.race} was born in the village. "
        elif fase == 1:
            self.defense = self.values["input"]
            if self.race == "Human":
                if self.defense.lower() == "karate":
                    self.defense = "karate"
                    return f"You've successfully learnt Karate!"
                else:
                    self.defense = "Fire Magic"
                    self.playing = False
                    return f"Due to your lack of magical skills, while learning {self.defense} you ended up getting killed in the first baby training fight!"
            else:
                if self.defense.lower() == "fire magic":
                    self.defense = "Fire Magic"
                    return f"You've successfully learnt Fire Magic!"
                else:
                    self.defense = "Karate"
                    self.playing = False
                    return f"Due to your lack of health as a witch, while learning {self.defense} you ended up getting killed in the first baby training fight!"
        elif fase == 2:
            help = self.values["input"]
            if help.lower() == "yes":
                self.DidHelp = True
                return f"The slime thanks you for helping him getting back to its familly."
            else:
                return f"You left the slime resolve its problems on its own."
        elif fase == 3:
            choice = self.values["input"].lower()
            if choice == "run":
                if self.DidHelp == False:
                    return f"The {self.race} tried to run, but they ended up being caught after being persecuted by the bad guys. You were killed (End)"
                elif self.DidHelp == True:
                    return f"The bad guys tried to get you, but the mother slime swalled them before they caught you. You ran (End)"
            else:
                if self.race == "Human":
                    return "The Human tries to fight, but they're week strength make him lose. You Died (End) " 
                else:
                    return f"The Witch successfully attacks the bad guy from distance with their {self.defense} and kills him. You won the fight (End)"
    
    def LerValores(self):
        self.event, self.values = self.window.Read()
        if self.event == "Começar":
            self.window.FindElement("Começar").Update("Enviar")



jogo = AdventureGame()
jogo.Iniciar()