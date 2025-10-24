def pedeNota():
    while True:
        try:
            nota = int(input("Digite uma nota entre 0 a 10: "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Esse numero é invalido!")
        except ValueError:
            print("Digite um valor entre 0 a 10!")


#Programa principal
while True:
    try:    
        menu = int(input("1 - Digitar uma nota de 0 a 10: "))
        if menu == 1:
            nota = pedeNota()
            print(f"A nota é {nota}!")

        else:
            print("Digite algo valido!")
            continue
        break
    except ValueError:
        print("Digite um valor valido!")