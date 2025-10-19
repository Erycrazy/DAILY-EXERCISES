from math import hypot

def calculoMatHI(caParam, coParam):
    hi = hypot(caParam, coParam)
    print(f"A hipotenusa é: {hi}")

def calculoSemMath(catAdjParam, catOpsParam):
    hip = (catOpsParam ** 2 + catAdjParam ** 2) ** (1/2)
    print(f"A hipotenusa sem math é: {hip}")

menu = int(input("1 - Calcular Hipotenusa com Math\n2 - Calcular Hipotenusa sem Math\nDigite o digito: "))


try:
    opção = int(menu)

    print("\n-----Digite os valores dos Catetos-----")
    catAdj = float(input("Digite o Cateto Adjacente: "))
    catOps = float(input("Digite o Cateto Oposto: "))

    if opção == 1:
        calculoMatHI(catAdj, catOps)

    elif opção == 2:
        calculoSemMath(catAdj, catOps)

    else:
        print("Digite um valor valido de 1 a 2!")

except ValueError:
    print("Entrada invalida, digite um numero valido de 1 a 2!")


