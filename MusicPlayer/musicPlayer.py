import utils.ApresentaçãoDoPrograma as apresentar
import utils.Options
from playsound import playsound
aP = apresentar.Apresentação()
opt = utils.Options.Options()

class MusicPlayer:
    def __init__(self):
        self.texto1 = (
""" This script is able to play musics, or at least it was supposed to.\n"""
)
        self.music = ""

    def iniciar(self):
        aP.Apresentar("Music Player", self.texto1)
        self.pedirMusica()

        try:
            playsound(f"musics\\{self.music}")
        except:
            print("Something went wrong, make sure you selected a valid option!")

    def pedirMusica(self):
        files, options = opt.Options()

        print(options)

        musicIndex = int(input("Selecione a sua opção:   "))
        self.music = files[musicIndex]
player = MusicPlayer()
player.iniciar()
