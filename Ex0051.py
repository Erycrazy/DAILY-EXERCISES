#Digiter um numero até dizer não, depois calcular a media e maior ou menor


try:
    
    contador = 0
    total = []
    while True:
        
        numero = int(input("Digite um numero: "))
        usuario = str(input("Quer continuar [S/N] ")).strip().upper()

        contador += 1
        total.append(numero)
            
        if usuario == "N":

            total_dos_valores = sum(total)
            media = total_dos_valores / contador
            maior_numero = max(total)
            menor_numero = min(total)
            print(f"O media é {media} e o maior numero foi: {maior_numero} e o menor foi: {menor_numero}")
            break
        
        


except ValueError:
    print("Digite um valor valido!")
    