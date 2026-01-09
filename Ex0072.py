nomes_e_pesos = [[], []]

while True:
    nome = str(input("Digite o nome: "))
    peso = int(input("Digite o peso: "))
    opcao = str(input("Quer continuar? [S|N]: ")).strip().upper()

    nomes_e_pesos[0].append(nome)
    nomes_e_pesos[1].append(peso)

    if opcao == "S":
        continue
    else:
        maior = max(nomes_e_pesos[1])
        menor = min(nomes_e_pesos[1])
        print(f"tem um total de: {len(nomes_e_pesos)}")
        print(f"O maior foi com {maior}")
        print(f"O menor foi {menor}")
        break



