lado01 = int(input("Digite o tamanho do primeiro lado do triangulo: "))
lado02 = int(input("Digite o tamanho do segundo lado do triangulo: "))
lado03 = int(input("Digite o tamanho do terceiro lado do triangulo: "))

if lado01 + lado02 > lado03:
    print("É posivel formar um triangulo!")

elif lado01 + lado03 > lado02:
    print("É possivel formar um triangulo!!")

elif lado02 + lado03 > lado01:
    print("É possivel formar um triangulo!!!")

    

else:
    print("Não é possivel formar um triangulo!")
