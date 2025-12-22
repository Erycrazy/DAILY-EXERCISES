#JOGO DO PAR OU IMPAR

from random import randint #importa o randint(valores randomicos para do tipo inteiro)


try:
    #Variaveis globais
    par_ou_impar = str(input("Escolhe [P/I]: ")).strip().upper()
    escolha_do_usuario = 0
    soma = 0
    contador = 0

    while "P" or "I":
        escolha_do_computador = randint(1, 10)

        #se for PAR acontece isso
        if par_ou_impar == "P":
            escolha_do_usuario = int(input("Fale um numero: "))
            soma = escolha_do_usuario + escolha_do_computador
            
            if soma % 2 == 0:
                contador += 1
                print(f"Você escolheu {escolha_do_usuario} e o Computador {escolha_do_computador} a soma deu {soma}\nVoce ganhou!")
                print("-"*20)
                continue

            else:
                print(f"Você escolheu {escolha_do_usuario} e o Computador {escolha_do_computador} a soma deu {soma}\nVoce perdeu!")
                #Aqui mostra os niveis para ver o quão bom vc é
                if 0 <= contador <= 2:
                    print("-"*20)
                    print(f"Tú é ruim, conseguir ganhar só {contador} vezes")

                elif 3 <= contador <= 4:
                    print("-"*20)
                    print(f"Tú até que não é ruim, consiguiu ganhar {contador} vezes")

                elif 5 <= contador <= 6:
                    print("-"*20)
                    print(f"Tú é bom mesmo ein!, tu conseguiu ganhar {contador} vezes!")
                
                elif contador > 6:
                    print("-"*20)
                    print(f"Meu parabéns!, você realmente é o melhor!, conseguiu ganhar {contador} vezes!")
                break

        #Se for IMPAR acontece isso
        if par_ou_impar == "I":
                escolha_do_usuario = int(input("Digite um numero: "))
                soma = escolha_do_usuario + escolha_do_computador

                if soma % 2 == 1:
                    contador += 1
                    print(f"Você escolheu {escolha_do_usuario} e o Computador {escolha_do_computador} a soma deu {soma}\nVoce ganhou!")
                    continue

                else:
                    print(f"Você escolheu {escolha_do_usuario} e o Computador {escolha_do_computador} a soma deu {soma}\nVoce perdeu!")
                    if 0 <= contador <= 2:
                        print("-"*20)
                        print(f"Tú é ruim, conseguir ganhar só {contador} vezes")

                    elif 3 <= contador <= 4:
                        print("-"*20)
                        print(f"Tú até que não é ruim, consiguiu ganhar {contador} vezes")

                    elif 5 <= contador <= 6:
                        print("-"*20)
                        print(f"Tú é bom mesmo ein!, tu conseguiu ganhar {contador} vezes!")
                    
                    elif contador > 6:
                        print("-"*20)
                        print(f"Meu parabéns!, você realmente é o melhor!, conseguiu ganhar {contador} vezes!")
                    break

except ValueError:
    print("Digite um valor valido!")
    