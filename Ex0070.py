#Separador de numeros pares e impares usando listas

lista_completa = []
lista_pares = []
lista_impares = []

while True:
    numero_usuario = int(input("Digite o valor: "))
    opcao = str(input("Você quer continuar [S|N]: ")).strip().upper()
    lista_completa.append(numero_usuario)
    
    if numero_usuario % 2 == 0:
        lista_pares.append(numero_usuario)

    if numero_usuario % 2 == 1:
        lista_impares.append(numero_usuario)

    if opcao == "S":
        continue

    else:
        print(f"A lista completa é {lista_completa}")
        print(f"A lista com os numeros pares é {lista_pares}")
        print(f"A lista com os numeros impares é {lista_impares}")
        break