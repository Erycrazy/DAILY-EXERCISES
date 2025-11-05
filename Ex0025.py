import datetime
while True:
    try:
                
        anoNasceu = int(input("Digite o ano que nasceu: "))
        anoAtual = datetime.date.today().year
        idade = anoAtual - anoNasceu

        if idade <= 9:
            print("MIRIM!")
            break
        elif idade <= 14:
            print("INFANTIL!")
            break
        elif idade <= 19:
            print("JUNIOR!")
            break
        elif idade <= 20:
            print("SENIOR!")
            break
        elif idade > 25:
            print("MASTER!")
            break
        else:
            print("Digite algo valido!")
            
    except ValueError:
        print("Digite um valor valido!")