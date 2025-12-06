#Verificador de Escolhas

while True:
    try:
        sexo = str(input("Digite [M|F] de for Masculino ou Feminino: ").upper())

        if sexo == "M":
            print("Você é homem")
            break

        if sexo == "F":
            print("Você é mulher!")
            break

    except ValueError:
        print("Digite um sexo valido!")
        continue