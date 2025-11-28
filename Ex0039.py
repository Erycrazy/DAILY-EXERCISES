#Verifica se é palindromo ou não

frase = str(input("Digite a frase: "))
palavras = frase.split()
junto = "".join(palavras)
inverso = junto[::-1]

print(f"O inverso de: {frase} || é: {inverso}")

if frase == inverso:
    print("Ela é palindroma")

else:
    print("Ela não é palindroma")