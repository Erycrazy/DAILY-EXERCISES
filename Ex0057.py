#CAIXA DE MERCADO

print("*"*20)
print("LOJA JEBA DURA")
print("*"*20)

try:
    #Variaveis globais
    produtos_maior_de_1000 = 0
    nomes_dos_produtos = []
    precos_dos_produtos = []

    while True:
        #inputs
        nome_do_produto = str(input("Diga o nome do produto: "))
        preco_do_produto = int(input("Diga o valor do produto: R$"))

        #enviam o valor para a lista vazia
        nomes_dos_produtos.append(nome_do_produto)
        precos_dos_produtos.append(preco_do_produto)

        #contador de produtos acima de 1000
        if preco_do_produto >= 1000:
            produtos_maior_de_1000 += 1

        continuar = str(input("Quer continuar [S|N]: ")).strip().upper()

        if continuar == "S":
            continue

        menor_preco = min(precos_dos_produtos) #menor valor da lista
        indice_menor = precos_dos_produtos.index(menor_preco) #posição do menor valor
        produto_mais_barato = nomes_dos_produtos[indice_menor] #nome do produto nessa posição
        preco_do_produto_mais_barato = min(precos_dos_produtos)     
        
        if continuar == "N":
            total_gasto = sum(precos_dos_produtos)
            print("-"*20)
            print(f"O total gasto foi {total_gasto:.2f}")
            print("-"*20)
            print(f"Tem {produtos_maior_de_1000} produtos que custam mais de R$1000")
            print("-"*20)
            print(f"O produto mais barato é: {produto_mais_barato} que custou: R${preco_do_produto_mais_barato}")
            print("-"*20)
            break

 


except ValueError:
    print("Digite um valor valido!")