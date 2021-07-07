import os

class Options:
    def __init__(self):
        self.path = ".\\musics"
        self.files = os.listdir(self.path)

    def Options(self):
        options = ""
        index = 0
        for filename in self.files:
            options += f"[{index}]     {filename}\n"
            index += 1
        options += "\n[S]     Sair\n"
        return self.files, options
