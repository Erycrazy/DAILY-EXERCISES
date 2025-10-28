while True:
    try:
        opcao = int(input("Digite\n1 - Binario\n2 - octal\n3 - Hexadecimal\n\nDigite o digito desejado: "))
        
        if opcao == 1:
            num = int(input("Digite o valor: "))
            print(f"O valor em binario é: {bin(num)[2:]}")
            break
        elif opcao == 2:
            num2 = int(input("Digite o valor: "))
            print(f"O valor em Octadecimal é: {oct(num2)[2:]}")
            break
        elif opcao == 3:
            num3 = int(input("Digite o valor: "))
            print(f"O valor em Hexadecimal é: {hex(num3)[2:]}")
            break
        else:
            print("Digite um valor valido!\n")
            continue

    except ValueError:
        print("Digite entre as opções 1, 2, 3")