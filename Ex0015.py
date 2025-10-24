while True:
    try:     
        nome = str(input("Digite um nome que tem mais que 3 caracteres: "))      
        if len(nome) > 3:
            print("Seu nome é bom")
            pass
        else:
            print("O nome tem que ter pelomenos 4 letras!")
            continue

    except ValueError:
        print("Digite algo valido por favor!")

    try:
        idade = int(input("Digite sua idade: "))

        if 0 <= idade >= 150:
            print("Boa idade!")
        else:
            print("Digite uma idade valida!")
            continue
    except ValueError:
        print("Digite algo valido!@")

    try:
        salario = int(input("Digite um digite seu salario: "))
        if salario <= 0:
            print("Bom salario!")

        else:
            print("Tá devendo é!?")
            continue
    except ValueError:
        print("Digite algo valido!#")

    try:
        sexo = str(input("""Digite "m" se for masculino e "f" se from feminino: """))
        if sexo == "m":
            print("Tu es MACHO!")

        elif sexo == "f":
            print("Femea es TÚ!?")

        else:
            print("Digite algo valido!%")
            continue

    except ValueError:
        print("Digite algo valido!$")

        estado = str(input("""Digite "s","c","v","d" para seu estado!: """))
        if estado == "s":
            print("Tu é de São paulo!")

        elif estado == "c":
            print("Tu és de Cantarolim do norte!")

        elif estado == "v":
            print("Tu és de Verdinha do norte!")

        elif estado == "d":
            print("Tu és de Deodoncio damasco!")

        else:
            print("Digite algo valido!")
            continue
    break
        




