soma = 0
contador = 0
for i in range(1, 500, +2):
    
    if i % 3 == 0:
        soma += i
        contador += 1 
print(f"A soma total dos {contador} numeros Impares multiplos de 3 até o 500 é: {soma}")