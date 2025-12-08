#Calculador / MAIOR / SAIR

while True:
    try:
        print("1 - SOMAR\n" \
        "2 - MULTIPLICAR\n" \
        "3 - MAIOR\n" \
        "4 - SAIR DO PROGRAMA\n")
        opcao = int(input("Digite o numero: "))

        match opcao:
            case 1:
                num1 = float(input("Digite um valor: "))
                num2 = float(input("Digite um segundo valor: "))
                print(f"A soma dos valores são: {num1+num2}")

            case 2:
                num1 = float(input("Digite um valor: "))
                num2 = float(input("Digite um segundo valor: "))
                print(f"A multiplicação dos valores são: {num1*num2}")
            
            case 3:
                num1 = float(input("Digite um valor: "))
                num2 = float(input("Digite um segundo valor: "))
                if num1 > num2:
                    print("O primeiro numero é maior!")

                elif num1 < num2:
                    print("O segundo numero é maior!")

                else:
                    print("Os dois são iguais!")

            case 4:
                print("Saindo...")
                break
                

    except ValueError:
        print("Digite um valor valido!")