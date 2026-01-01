#Exercicio de teste com enumerate

from random import randint

lista = list(randint(0,9) for i in range(5))

if 5 in lista:
    lista.remove(5)
    print("O numero 5 foi removido!")

else:
    lista.append(5)
    print("O cinco foi colocado a lista!")

print(lista)

for posicao, valor in enumerate(lista):
    print(f"Na posição {posicao} está o numero {valor}")