#Ledor de numeros que mostra a soma e qts no final

soma = 0
contador = 0
numeros = []
while True:
    numero = int(input("Digite um numero: "))
    contador += 1
    numeros.append(numero)
    if numero == 999:
        soma = sum(numeros[:-1])
        print(f"A quantidade de vezes digitada for: {contador} e a soma é: {soma}")
        break
    else:
        print("Digite um valor valido!")
        continue