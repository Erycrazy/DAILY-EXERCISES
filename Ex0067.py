#Digitar valores sem repetição

lista = []

while True:
    valor_para_lista = int(input("Digite um numero: "))
    continuar = str(input("Você quer continuar? [S|N]: ")).strip().upper()

    lista.append(valor_para_lista)
    if continuar == "S":
        continue
    
    else:
        lista_unica = list(set(lista))
        lista_unica.sort()
        print(f"A lista sem valores repetidos é: {lista_unica}")

    