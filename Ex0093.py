def leia_int(numero):
    while True:
        try:
            valor_retornado = int(input(numero)); 
            return valor_retornado; 
        except ValueError:
            print("ERRO: Digite um numero!"); 
    
n = leia_int("O valor é: "); 
print(f"Você acabou de digita o numero {n}"); 