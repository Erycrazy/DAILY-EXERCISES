#JOGO DA ADIVINHAÇÃO COM REPETIÇÃO

import random

lista_computador = [1,2,3,4,5,6,7,8,9,10]
escolha_do_computador = random.choice(lista_computador)
contador = 0

while True:
    try:
        escolha_do_usuario = int(input("Digite um numero: "))

        if escolha_do_usuario == escolha_do_computador:
            print("")
            print("Parabens, você acertou!")
            print("*"*20)
            print(f"Numero escolhido foi {escolha_do_computador}")
            print("")
            print(f"Você necessitou de {contador} tentativas para acertar!")
            break

        else:
            print("Tente novamente!")
            contador += 1
            continue

    except ValueError:
        print("Digite algo valido!")