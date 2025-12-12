#Sequencia de fibonacci
while True:
    try:
        num = int(input("Quantos termos de fibonacci você quer ver: "))

        if num < 3:
            print("Digite um número no mínimo 3 para cima!")
            continue

        primeiro_termo = 0
        segundo_termo = 1
        contador = 0

        print("Sequência de Fibonacci:", end=" ")
        while contador < num:
            print(f"{segundo_termo}", end=", " if contador < num - 1 else "\n")

            terceiro_termo = primeiro_termo + segundo_termo
            primeiro_termo = segundo_termo
            segundo_termo = terceiro_termo
            contador += 1
            
    except ValueError:
        print("Digite um valor valido!")