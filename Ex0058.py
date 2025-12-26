#Caixa de Banco

print('=' * 30)
print('{:^30}'.format('BANCO Edcley Negocios'))
print('=' * 30)
try:
    valor = int(input("Digite o valor que quer sacar: R$ "))
    total = valor
    cedula = 50
    total_cedula = 0

    while True:
        if total >= cedula:
            total -= cedula
            total_cedula += 1

        else:
            if total_cedula > 0:
                print(f"Total de {total_cedula} cédulas de R${cedula}")

            if cedula == 50:
                cedula = 20

            elif cedula == 20:
                cedula = 10

            elif cedula == 10:
                cedula = 1

            total_cedula = 0
            if total == 0:
                break
except ValueError:
    print("Digite um valor valido!")