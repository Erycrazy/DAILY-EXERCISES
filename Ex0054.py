#Tabuada que para com valores negativos

while True:
    numero_da_tabuada_usuario = int(input("Digite um numero que quer ver a tabuada: "))

    for num in range(1, 10):
        tabuada = numero_da_tabuada_usuario * num
        print(f"A tabuada de {numero_da_tabuada_usuario} é: {numero_da_tabuada_usuario} X {num} = {tabuada}")
        continue

    if numero_da_tabuada_usuario < 0:
        print("ENCERRANDO PROGRAMA...")
        break