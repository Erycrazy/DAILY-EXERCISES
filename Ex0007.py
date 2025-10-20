nome = str(input("Digite seu nome: "))

print(f"""
Seu nome me maiusculo é: {nome.upper()}
Seu nome em minusculo é: {nome.lower()}
Seu nome tem : {len(''.join(nome.split()))} letras
Seu primeiro nome tem: {len(nome.split())} letras""")
