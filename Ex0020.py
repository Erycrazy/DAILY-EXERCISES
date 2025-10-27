casa = float(input("Valor casa: "))
salario = float(input("Valor salário: "))
anos = int(input("Qnts anos: "))
prestação = casa / (anos * 12)
os30Porcento = salario * 0.30
print(f"Para pagar uma casa de {casa:.2f} em {anos}, a prestação será de R${prestação:.2f}")

if prestação <= os30Porcento:
    print("CONCEDIDO!")

else:
    print("NEGADO!")
    