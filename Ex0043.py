#Vê nome, idade, e sexo, assim mostra media, quem é o homem mais velho e mulher -20 anos

nome = []
idade = []
sexo = []
mulheres_menor_20 = 0
mais_velho = 0
mais_velho02 = ""

for i in range(2):
    nomes = input("Digite seu nome: ")
    idades = int(input("Digite sua idade: "))
    sexos = input("Digite se é 'mulher' ou 'homem': ").strip().lower()

    nome.append(nomes)
    idade.append(idades)
    sexo.append(sexos)

    # Verifica se é mulher com menos de 20
    if sexos == "mulher" and idades < 20:
        mulheres_menor_20 += 1

    # Verifica se é homem e é o mais velho até agora
    if sexos == "homem" and idades > mais_velho:
        mais_velho = idades
        mais_velho02 = nomes

# Após o laço, calcular a média
media = sum(idade) / len(idade)

print(f"A média de idades é: {media:.2f}")
print(f"O homem mais velho é: {mais_velho02}")
print(f"Tem exatamente {mulheres_menor_20} mulher(es) com menos de 20 anos.")