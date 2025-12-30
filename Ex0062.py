#Tabela de preços e nomes

tupla_de_precos = ("Pão", 3.50, "Leite", 4.20, "Café", 7.00, "Sorvete", 3.00)

print("-="*20)
print(f"{'TABELA DE PREÇOS':^35}")
print("-="*20)

for posicao in range(0, len(tupla_de_precos)):
    if posicao % 2 == 0:
        print(f"{tupla_de_precos[posicao]:.<30}", end="")
    else:
        print(f"R${tupla_de_precos[posicao]:.>5}")
