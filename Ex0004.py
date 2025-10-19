from math import hypot;

def calculoMathHI(caParam, coParam, hiParam):

    ca = float(input("Digite o cateto adjacente: "))
    co = float(input("Digite o cateto oposto: "))

    hi = hypot(ca, co)

    print(f"A hipotenusa é {hi}")


def CalculoSemMath(catAdjParam, catOpsParam, hipParam):
    catAdj = float(input("Digite o cateto Adjacente: "))
    catOps = float(input("Digite o cateto Oposto: "))

    hip = (catOps ** 2 + catAdj ** 2) **(1/2)

    print(f"A hipotenusa é: {hip}")

menu = input("1 - Calcular Hipotenusa com Math\n2 - Calcular Hipotenusa sem Math\n")

if int(menu) == 1:
    calculoMathHI(caParam=any, coParam=any, hiParam=any)

elif int(menu) == 2:
    CalculoSemMath(catAdjParam=any, catOpsParam=any, hipParam=any)

else:
    print("Digite uma opção valida. Um numero de 1 a 2!")