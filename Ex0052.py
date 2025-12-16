#PA V3

primeiro = int(input("Primeiro termo: ")) #Começa em
razao = int(input("Digite a Razão: "))#Pulando de
termo = primeiro
contador = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while contador <= total:
        print(termo)
        termo += razao
        contador += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar quantos a mais?: "))
print(f"progressão finalizada com {total} termos mostrados")