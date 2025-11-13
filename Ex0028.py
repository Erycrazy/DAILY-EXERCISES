valorAPagar = int(input("Digite o valor a pagar na conta: "))

opcao = int(input("1 - a vista\n2 - cartão 5% desc.\n3 - 2x no cartão\n4 - 3x ou mais no cartão\n\nDigite o digito: "))


if opcao == 1:
    valorDescontado = valorAPagar - (valorAPagar * 0.10)
    print(f"Valor a pagar: {valorDescontado}")

elif opcao == 2:
    valorDescontadoCartao = valorAPagar - (valorAPagar * 0.05)
    print(f"Valor a pagar é: R${valorDescontadoCartao}")

elif opcao == 3:
    valorNormal = valorAPagar / 2
    print(f"Terá que pagar 2x de R${valorNormal}")

elif opcao == 4:
    vezesCartao = int(input("Quantas vezes no cartão: "))
    valorComJuros = valorAPagar + (valorAPagar * 0.20)
    prestacao = valorComJuros / vezesCartao
    if vezesCartao > 24:
        print("Não pode ultrapassar 24x no cartão!")
        
    else:
        print(f"Custará {vezesCartao}x de R${prestacao}")
        print(f"Valor total a pagar será de: R${valorComJuros}")

else:
    print("Digite um valor valido!")