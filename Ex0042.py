#Vê qual é o maior e menor peso em 5 pessoas

pesos = []

for i in range(5): #Dá para colocar (1, 6) e mudar a variavel em peso somente como i
    peso = float(input(f"Digite seu {i+1} peso: ")) 
    pesos.append(peso)
    maior = max(pesos)
    menor = min(pesos)
    

print(f"O maior peso é {maior}")
print(f"O menor peso é {menor}")