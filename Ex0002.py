class CalculadorPeixe:
    def contadorPeixe():
        pesoPeixe = float(input("Peso do peixe: "))
        excesso = pesoPeixe - 50
        multa = 4.0

        if pesoPeixe <= 50:
            print("OK, está dentro do peso permitido!")

        elif pesoPeixe > 50:
            print(f"O excesso foi de: {excesso}")

        if pesoPeixe > 50:
            multaPagar = excesso * multa
            print(f"A multa fica em {multaPagar}")


print(CalculadorPeixe.contadorPeixe())