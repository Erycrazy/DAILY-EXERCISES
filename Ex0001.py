
class Operadores:

    def operadorSoma(num1, num2):
        return num1 + num2

    def operadorSub(num1, num2):
        return num1 - num2

    def operadorMulti(num1, num2):
        return num1 * num2

    def operadoDivi(num1, num2):
        return num1 / num2
    
num1 = float(input(f"Digite seu primeiro numero que quer calcular: "))
num2 = float(input(f"Digite seu segundo numero que quer calcular: "))

operador = float(input("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\nDigite o operador: "))

if operador == 1:
    resultado = Operadores.operadorSoma(num1, num2)

elif operador == 2:
    resultado = Operadores.operadorSub(num1, num2)

elif operador == 3:
    resultado = Operadores.operadorMulti(num1, num2)

elif operador == 4:
    resultado = Operadores.operadoDivi(num1, num2)

else:
    print("Opção invalida!, Digite um numero de 1 a 4!")

print(f"Resultado: {resultado}")