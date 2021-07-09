#   Codificador simples em que se insere uma string e é devolvido a mesma, contudo em transformada em um código através da chave inserida pelo usuário (ex: 6,-1,3)
#
#   Dica: Para descodificar algo, também é possível escrever a mesma chave mas com os sinais inversos, no caso do exemplo anterior seria "-6,1,-3"

from utils.dicts import LetterToNumber
from utils.dicts import NumberToLetter

class enCoder:
    def __init__(self):
        self.input_string = ""
        self.array_code = []
        self.voltas = 0
    def start(self):
        self.input_string = input("Insira a frase a codificar: ")
        self.Key = input("Insira a chave (3 digitos separados por ',' sem espaços): ").split(",")
        print(self.encode(self.input_string))

    def encode(self, stringToEncode):
        for char in stringToEncode:
            try:
                char = self.ApplyKey(LetterToNumber[char.upper()])
                self.array_code.append(NumberToLetter[char])
            except:
                char = self.ApplyKey(char)
                self.array_code.append(char)
        return "".join(self.array_code)
            
    def ApplyKey(self, char):
        if isinstance(char, int):
            if self.voltas == 0:
                char += int(self.Key[0])
                self.voltas += 1
                return self.FixValue(char)
            elif self.voltas == 1:
                char += int(self.Key[1])
                self.voltas += 1
                return self.FixValue(char)
            else:
                char += int(self.Key[2])
                self.voltas = 0
                return self.FixValue(char)
        else:
            return char
    
    def FixValue(self, char):
        if char <= 25 and char >= 0:
            return char
        elif char > 25:
            char -= 26
            return char
        elif char < 0:
            char += 26
            return char
      

        


turing = enCoder()
turing.start()