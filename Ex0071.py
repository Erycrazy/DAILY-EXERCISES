#Verificador de expressão numerica(verifica sé é valida ou não)

expressao = str(input("Digite sua expressão: "))
lista = []

for simbolo in expressao:
    if simbolo == "(":
        lista.append("(")

    elif simbolo == ")":
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(")")
            break
if len(lista) == 0:
    print("Sua expressão está valida!")
else:
    print("Sua expressão está invalida!")

    