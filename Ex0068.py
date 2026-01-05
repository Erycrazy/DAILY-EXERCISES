#Lendo 5 valores e organizando sem usar sort()

    
lista = []

for valor in range(0, 5):
    numero = int(input("Digite o valor: "))
    if valor == 0 or numero > lista[-1]:
        lista.append(numero)

    else:
        posicao = 0
        while posicao < len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                break
            posicao += 1

print(f"O valores digitados na lista é: {lista}")