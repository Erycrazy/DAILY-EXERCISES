#Lendo uma PA V2

primeiro = int(input("Primeiro termo: ")) #Começa em
razao = int(input("Digite a Razão: "))#Pulando de
termo = primeiro
contador = 1

while contador <= 10:
    print(termo)
    termo += razao
    contador += 1

print("FIM")



