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

            os.system("cls")

                            
    def pedirMusica(self):
        
        files, options = opt.Options()
        self.playlist = False

        print(options)
        PlaylistIndexes = (input("Select yout option:   "))
        if PlaylistIndexes.lower() != "x":
            loop = input("Loop? (Y/n)    ")
            while True:
                
                    for musicI in PlaylistIndexes:
                        try:
                            self.music = files[int(musicI)]
                            self.Tocar()
                        except:
                            print("Something went wrong, make sure you selected a valid option!")
                            self.playing = 0
                            self.options = ""
                    if loop.lower() != "y":
                        break
        else:
            self.stop = True
            os.system("cls")
             
        
                
                
    def Tocar(self):
        winsound.PlaySound(f"musics\\{self.music}", winsound.SND_ALIAS)

player = MusicPlayer()
player.iniciar()
