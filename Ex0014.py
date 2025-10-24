while True:
    try:
        nome = str(input("Digite seu mome: "))
        senha = str(input("Digite sua senha: "))
        if nome in senha:
            print("Por sua segurança, sua senha não pode conter seu nome!")

        else:
            print("Senha forte")
            break

    except ValueError:
        print("Digite uma valor valido!")