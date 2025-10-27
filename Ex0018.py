while True:
    try:    
        num1 = int(input("Digite um numero: "))

        if num1 % 2 != 0:
            print("Impar!")

        else:
            print("par!")

    except ValueError:
        print("Valor invalido!")