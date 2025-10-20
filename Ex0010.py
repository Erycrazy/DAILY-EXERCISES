num = int(input("Digite um numero de 0 a 9999! "))
u = num // 1 % 10  #Se dividir por 1, vai mostrar os 4 primeiros digitos, 
d = num // 10 % 10   #Mas se colocar o resto(%)    
c = num  // 100 % 10 #Da divisão por 10 ele mostra so o ultimo digito!
m = num // 1000 % 10
# mostra as unidades
print(f"A unidade é: {u}")
print(f"A dezena é: {d}")
print(f"A centena é: {c}")
print(f"A milhar é: {m}")