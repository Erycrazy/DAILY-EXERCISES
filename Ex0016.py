from random import randint

while True:

    try:
        numA = randint(1, 5) #Se usar a biblioteca inteira se usa ramdom.radint(1, 5)
        numPede = int(input("Digite um numero para ver se acerta!: "))
        if numPede == numA:
            print(f"O Numero escolhido foi: {numA}")
            print("Parabens, você acertou!")
            break
        else:
            print("Tente novamente!")

    except ValueError:
        print("Digite um valor valido!")