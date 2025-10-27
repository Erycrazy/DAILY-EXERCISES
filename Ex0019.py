while True:
    try:
        distancia = float(input("Digite a distancia que ira percorrer: "))
        
        if distancia < 150:
            taxa = distancia * 0.60
            print(f"A taxa a pagar é de R${taxa:.2f}")
            break
        elif distancia >= 150:
            taxa = distancia * 0.50
            print(f"A taxa a pagar: R${taxa:.2f}")
            break
        elif distancia >= 200:
            taxa = distancia * 0.40
            print(f"A taxa a pagar: R${taxa:.2f}")
            break
        elif distancia >= 500:
            taxa = distancia * 0.20
            print(f"A taxa a pagar é de: {taxa:.2f}")
            break
        else:
            print("Digite algo valido!")
            continue
    except ValueError:
        print("Digite um numero!")