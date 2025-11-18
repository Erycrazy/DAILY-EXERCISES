while True:
    try:
        print("*"*20, "METRICA PARA VER SE 3 SEGMENTOS FORMAM UM TRIÂNGULO", "*"*20)
        reta01 = float(input("Primeiro segmento: "))
        reta02 = float(input("Segundo segmento: "))
        reta03 = float(input("Terceiro segmento: "))

        if reta01 < reta02 + reta03 and reta02 < reta01 + reta03 and reta03 < reta01 + reta02:
            print("Dá pra formar um triangulo!")

            if reta01 == reta02 and reta02 == reta03: #Dá par colocar reta01 == reta02 == reta03: só o py aceita isso!
                print("Este triangulo é Equilatero!")
                break
            elif reta01 != reta02 and reta02 != reta03 and reta03 != reta01:
                print("Este triangulo é Escaleno!")
                break
            else:
                print("Este triangulo é Isoseles!")
                break
        else:
            print("Não dá pra fazer um triangulo!")

    except ValueError:
        print("Digite algo valido!")