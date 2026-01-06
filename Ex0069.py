#Mostra lista no decrescente, se 5 está na lista, e a qnt de valores

lista = []

while True:
    try:
        numero = int(input("Digite o valor: "))
        lista.append(numero)
        quantidade_de_numeros_na_lista = len(lista)
        lista.sort(reverse=True)
        opcao = str(input("Você quer continuar [S|N]: ")).strip().upper()
    except ValueError:
        print("Digite algo valido!")
        continue
    if opcao == "S":
        continue
    else:

        if 5 in lista:
            print("O 5 está na lista!")
            break

        else:
            print("Não tem numero 5 na lista!")
            break

print(f"Foram digitados {quantidade_de_numeros_na_lista} numeros!")
print(f"A ordem decrescente é {lista}")



