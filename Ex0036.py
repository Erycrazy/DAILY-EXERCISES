soma = 0
numeros = []


for i in range(1, 7):
    num = int(input("Digite um numero: "))
    numeros.append(num)
    
    pares = [n for n in numeros if n % 2 == 0]

    soma = sum(pares)
print(f"A soma dos numeros pares é: {soma}")

# Jeito faz facil e simplificado de fazer a soma dos 6 numeros pares

soma = 0

for i in range(1, 7):
    i = int(input("Digite um numero: "))
    if i % 2 == 0:
        soma+= i
print(soma)
