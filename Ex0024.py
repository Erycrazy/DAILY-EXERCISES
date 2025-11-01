nota01 = int(input("Digite a nota do primeiro aluno: "))
nota02 = int(input("Digite a nota do primeiro aluno: "))
media = (nota01 + nota02) / 2

while True:
    try:
        if media >= 7:
            print("Aprovado!")
            break

        elif 5 <= media <= 6.9:
            print("Está de recuperação!")
            break

        elif media < 5:
            print("Reprovado!")
            break

        else:
            print("Digite algo valido!")
            continue

    except ValueError:
        print("Digite um valor valido!")
