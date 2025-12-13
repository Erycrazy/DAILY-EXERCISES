#Valor até 999 até parar, soma total dos valores menos o 999

primeiro_valor = 0
soma_da_lista = 0
contador = 0
lista = []

while primeiro_valor != 999:
    primeiro_valor = int(input("Digite um valor para começar: "))
    contador += 1
    primeiro_valores = lista.append(primeiro_valor)
    soma_da_lista = sum(lista[:-1])



print(f"A quantidade de vezes digitadas é: {contador - 1}\nSoma total é: {soma_da_lista}")
