while True:
    try:
        priNum = int(input("Digite o seu primeiro valor: "))
        segNum = int(input("Digite o seu segundo valor: "))

        if priNum > segNum:
            print("O primeiro valor é maior!")
            break
        elif segNum > priNum:
            print("O segundo valor é maior!")
            break
        else:
            print("Os dois são iguais!, não existem numeros maiores!")
            break

    except ValueError:
        print("Valor invalido!")