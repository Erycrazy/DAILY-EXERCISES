#Analise de dados e cadastro

contador_idade01 = 0
contador_idade02 = 0
contador_homems = 0
contador_mulheres = 0

while True:
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo [M|F]: ")).strip().upper()


    if sexo == "M": 
        print("-"*50)
        print("PESSOA CADASTRADO!")
        print("-"*50)
        if idade >= 18:
            contador_idade02 += 1
        contador_homems += 1

    if sexo == "F":
        print("-"*50)
        print("PESSOA CADASTRADO!")
        print("-"*50)
        if sexo == "F" and idade < 20:
            contador_mulheres += 1
        
    continuar = str(input("Quer continuar [S|N]: ")).strip().upper()

    if continuar == "S":
        continue

    total_pessoas = contador_idade01 + contador_idade02

    if continuar == "N":

        print("-"*50)
        print(f"Tem {total_pessoas} pessoas maior de idade cadastrados")
        print("-"*50)
        print(f"Tem {contador_homems} homems cadastrados")
        print("-"*50)
        print(f"Tem {contador_mulheres} mulheres abaixo dos 20 anos cadastrado")
        print("-"*50)
        break


