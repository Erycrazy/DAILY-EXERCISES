#Pedra Papel Tesoura

import time
import random
while True:
    try:
        ppt = ["PEDRA", "PAPEL", "TESOURA"]
        escolhaComputador = random.choice(ppt)

        opcao = int(input("Suas Opções:\n\n1 - PEDRA\n2 - PAPEL\n3 - TESOURA\n\nDigite a sua escolha: "))

        print("*"*50)
        time.sleep(0.5)
        print("JO")
        time.sleep(0.5)
        print("KEN")
        time.sleep(0.5)
        print("PO!!!")
        print("*"*50)

        if opcao == 1:

            if opcao == 1 and escolhaComputador == "TESOURA":
                print(f"Computador: {escolhaComputador.upper()}!")
                print(f"Você: PEDRA!")
                print("GANHOU!")
                break

            elif opcao == 1 and escolhaComputador == "PAPEL":
                print(f"Computador: {escolhaComputador.upper()}!")
                print(f"Você: PEDRA!")
                print("PERDEU!")
                break

            elif opcao == 1 and escolhaComputador == "PEDRA":
                print(f"Computador: {escolhaComputador.upper()}!")
                print(f"Você: PEDRA!")
                print("EMPATE!")
                break

        elif opcao == 2:

            if opcao == 2 and escolhaComputador == "PEDRA":
                print(f"Computador: {escolhaComputador.upper()}!")
                print(f"Você: PAPEL!")
                print("GANHOU!")
                break

            elif opcao == 2 and escolhaComputador == "TESOURA":
                print(f"Computador: {escolhaComputador.upper()}!")
                print(f"Você: PAPEL!")
                print("PERDEU!")
                break
            elif opcao == 2 and escolhaComputador == "PAPEL":
                print(f"Computador: {escolhaComputador.upper()}!")
                print(f"Você: PAPEL!")
                print("EMPATE!")
                break
        elif opcao == 3:

            if opcao == 3 and escolhaComputador == "PAPEL":
                print(f"Computador: {escolhaComputador.upper()}!")
                print(f"Você: TESOURA!")
                print("GANHOU!")
                break
            elif opcao == 3 and escolhaComputador == "PEDRA":
                print(f"Computador: {escolhaComputador.upper()}!")
                print(f"Você: TESOURA!")
                print("PERDEU!")
                break
            elif opcao == 3 and escolhaComputador == "TESOURA":
                print(f"Computador: {escolhaComputador.upper()}!")
                print(f"Você: TESOURA!")
                print("EMPATE!")
                break
        else:
            print("Digite um valor valido!")
            continue

    except ValueError:
        print("Digite um valor valido!")
        