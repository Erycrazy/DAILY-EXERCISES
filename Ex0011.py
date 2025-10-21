nome = str(input("Digite seu nome completo: ")).lower().strip()

print(f"A letra A aparece {nome.count('a')} Vezes")
print(f"A primeira letra A apareceu na posição: {nome.find('a')+1}")
print(f"A ultima letra A apareceu na posição: {nome.rfint('a')+1}")