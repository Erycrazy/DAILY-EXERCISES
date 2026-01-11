par_e_impar = [[], []]

for valor in range(7):
    valores = int(input(f"Digite o {valor+1}° valor: "))
    if valores % 2 == 0:
        par_e_impar[0].append(valores)
        
    if valores % 2 == 1:
        par_e_impar[1].append(valores)
        
print(f"Os valores pares são: {par_e_impar[0]}")
print(f"Os valores impares são: {par_e_impar[1]}")