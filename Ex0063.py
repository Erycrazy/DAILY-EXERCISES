#Mostra vogais

palavras = ("aprender", "andar", "chorar", "bancar", "vedacao")

for palavra in palavras:
    print(f"\nNa palavra {palavra.upper()} temos:", end="")
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end="")

