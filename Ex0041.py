for i in range(5):
    peso = float(input(f"Digite o {i+1} peso: "))
    if i == 0:
        maior = peso
        menor = peso

    else:
        if peso > maior:
            maior = peso

        if peso < menor:
            menor = peso

print(f"O maior peso foi {maior}")
print(f"O menor peso foi {menor}")


