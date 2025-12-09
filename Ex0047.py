#Fatoração de numeros

from math import factorial

while True:
    try:
        num = int(input("Digite o numero que quer fatorar: "))
        fatorial = factorial(num)
        if fatorial >= 0:
            print(f"O fatorial do numero {num} é {fatorial}")
            break
        else:
            print("Não exite fatorial e numero negativos!")
            continue

    except ValueError:
        print("Digite um valor valido!")


#outra forma de fazer usando for:

# num = int(input("Digite o numero: "))
# if num == 1:
#     print(num)
# resultado = 1

# for i in reversed(range(num)):
#     resultado = resultado * (i + 1)
#     print(resultado)