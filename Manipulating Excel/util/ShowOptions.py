def printOptions(opts, type = 0):
    strToPrint= ""
    i = 0
    for opt in opts:
        strToPrint += f"[{i}]  {opt}\n"
        i += 1
    if type == 0:
        strToPrint += "\n[S]  Sair"
    print(strToPrint)