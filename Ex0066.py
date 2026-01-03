#Maior e menor valor de uma lista com posição

lista = []
for numero in range(5):
    numeros = int(input(f"Digite o {numero+1} valor: ") )
    lista.append(numeros)

for posicao, valor in enumerate(lista):
    print(f"A posição é {posicao} do valor {valor}\n")

maior_valor = max(lista)
menor_valor = min(lista)

print(f"O maior valor é {maior_valor}\nE o menor é {menor_valor}")