#Primeiro termo e a razão de uma PA

primeiro = int(input("Primeiro termo: ")) #Começa em
razao = int(input("Digite a Razão: "))#Pulando de
decimo = primeiro + (10 - 1) * razao

for i in range(primeiro, decimo + razao, razao):
    print(f"{i}")
