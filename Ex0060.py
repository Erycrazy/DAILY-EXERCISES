#Coloca numeros aleatorios dentro de uma tupla

from random import randint

tupla = tuple(randint(i + 1, 9) for i in range(5))

menor_valor = min(tupla)
maior_valor = max(tupla)

print(tupla)
print(f"O menor valor é: {menor_valor}, O maior valor é: {maior_valor}")