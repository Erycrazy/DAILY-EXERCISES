import datetime
while True:
    try:
        anoNasceu = int(input("Digite o ano que nasceu: "))
        anoAtual = datetime.date.today().year
        idade = anoAtual - anoNasceu

        sexo = str(input("""Digite "f" se for Mulher ou "m" se for Homem: """)).lower().strip()
        
        if sexo == 'f':
            print("Você não precisa fazer o alistamento obrigatorio!")
            break
        if sexo == 'm':     

            if idade == 18:
                print("Já tem idade para se alistar!")
                break
            
            elif idade > 18:
                tempoRestante = idade - 18
                ano = anoAtual - tempoRestante
                print(f"Você ja passou {tempoRestante} anos do que ja deveria!")
                print(f"Seu alistamento foi em {ano}")
                break
            elif idade < 18:
                tempoRestante02 = 18 - idade
                ano02 = anoAtual + tempoRestante02
                print(f"Ainda faltam {tempoRestante02} anos para o alistamento!")
                print(f"Seu alistamento será em {ano02}")
                break
            
        else:
            print("Digite algo valido!")
            continue
            
    except ValueError:
        print("Digite um valor valido!")