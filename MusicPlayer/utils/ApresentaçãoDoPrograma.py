class Apresentação:
    def __init__(self):
        pass
    
    def Apresentar(self, titulo, texto = ""):
        print(f"""
            {"=" * (36 + len(titulo) )}
            {"-" * 17} {titulo} {"-" * 17}
            {"=" * (36 + len(titulo) )}""")
        if texto != "":
            print(f"""
{texto}
            """)

