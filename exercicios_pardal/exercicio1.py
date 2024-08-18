def buscando_senha():
    with open("darkweb2017-top.txt", "r") as arquivo:
        alace = arquivo.readlines()
        for a in range(min(10, len(alace))):
            print(alace[a])
        


buscando_senha()