#Quantas vezes aparece o valor 9, armazena valor dentro da tupla e mostra o par

tupla = tuple(int(input(f"Digite o {i+1} valor: ")) for i in range(5))

qnts_vezes_aparece_nove = tupla.count(9)




print("-"*20)
print(f"Aparece o nove {qnts_vezes_aparece_nove} vezes")
print("-"*20)
if 3 in tupla:
    num_tres = tupla.index(3)+1
    print(f"O numero três está na posição {num_tres}")

else:
    print("Numero 3 não está na tupla")
print("-"*20)



for elemento in tupla:
    if elemento % 2 == 0:
        print("-"*20)
        print(f"Esse valor é par: {elemento}")