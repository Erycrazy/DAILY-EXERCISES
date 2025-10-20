from random import shuffle
from random import choice

def nomeEscolhido(n1Param, n2Param, n3Param, n4Param):
    lista = [n1Param, n2Param, n3Param, n4Param]
    escolhido = choice(lista)

    print(f"O aluno escolhido é o: {escolhido}!")

def embaralharNomes(nome01Param, nome02Param, nome03Param, nome04Param):
    lista01 = [nome01Param, nome02Param, nome03Param, nome04Param]

    shuffle(lista01)
    print(f"A ordem escolhida é: {lista01}")

menu = input("1 - Sorteia um nome aleatorio!\n2 - Mostra a ordem dos nomes!\n\nDigite o que quer fazer: ")
opcao = int(menu)

try:
    if opcao == 1:
        n1 = str(input("Digite o Nome do primeiro: "))
        n2 = str(input("Digite o Nome do segundo: "))
        n3 = str(input("Digite o Nome do terceiro: "))
        n4 = str(input("Digite o Nome do quarto: "))
        nomeEscolhido(n1, n2, n3, n4)

    elif opcao == 2:
        nome01 = str(input("Digite o Nome do primeiro: "))
        nome02 = str(input("Digite o Nome do segundo: "))
        nome03 = str(input("Digite o Nome do terceiro: "))
        nome04 = str(input("Digite o Nome do quarto: "))

        embaralharNomes(nome01, nome02, nome03, nome04)

    else:
        print("Numero invalido, digite 1 ou 2!")

except ValueError:
    print("Numero invalido!")    

