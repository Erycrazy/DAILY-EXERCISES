while True:
    try:

        peso = float(input("peso em KGs: "))
        altura = float(input("Altura em Metros: ")) 

        if altura.is_integer():
            altura = altura / 100

        imc = peso / (altura * altura)

        if imc < 1:
            print("Um átomo é mais pesado que tu!")

        elif imc < 5:
            print("Tu ta só o osso ou menos!")

        elif imc < 10:
            print("Vai procurar um medico!")

        elif imc < 18.5:
            print("Abaixo do peso")

        elif 18.5 <= imc < 25:
            print("peso ideal!")

        elif 25 <= imc < 30:
            print("Sobrepeso")

        elif 30 <= imc < 40:
            print("Obeso")

        elif imc > 40:
            print("Obesidade morbida!")

        else:
            print("Valor invalido!")

        print(imc)

    except ValueError:
        print("Digite valor valido!")