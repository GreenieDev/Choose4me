import os

class Options:
    def __init__(self):
        self.path = ".\\musics"
        self.files = os.listdir(self.path)
        self.options = ""

    def Options(self):
        index = 0
        for filename in self.files:
            self.options += f"[{index}]     {filename}\n"
            index += 1
        self.options += "\n"
        return self.files, self.options
