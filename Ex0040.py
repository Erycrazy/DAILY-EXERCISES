#Soma as quantidades de pessoas maiores e menores de idade

maior_de_idade = 0
menor_de_idade = 0
for i in range(1, 8):
    i = int(input("Digite o ano que nasceu: "))
    idade = 2025 - i
    if idade > 18:
        maior_de_idade += 1

    elif idade < 18:
        menor_de_idade += 1
print(f"Os menores de idade são: {menor_de_idade}\nOs maiores de idade são: {maior_de_idade}")
