import utils.ApresentaçãoDoPrograma as apresentar
import utils.Options
import os, winsound
aP = apresentar.Apresentação()
opt = utils.Options.Options()

class MusicPlayer:
    def __init__(self):
        self.texto1 = (
""" This script is able to play musics, or at least it was supposed to.\n"""
)
        self.music = ""
        self.playing = 1
        self.stop = False

    def iniciar(self):
        while self.stop == False:
            self.playing = 1
            aP.Apresentar("Music Player", self.texto1)
            self.pedirMusica()
            if self.stop == False:
                if self.playing == 1:
                    winsound.PlaySound(f"musics\\{self.music}", winsound.SND_ALIAS)
                    print("Acabou!")
                os.system("cls")
                    


    def pedirMusica(self):
        
        files, options = opt.Options()

        print(options)
        try:
            musicIndex = (input("Selecione a sua opção:   "))
            if musicIndex == "S":
                self.stop = True
            else:
                
                self.music = files[int(musicIndex)]
        except:
            print("Something went wrong, make sure you selected a valid option!")
            self.playing = 0
            self.options = ""
player = MusicPlayer()
player.iniciar()
