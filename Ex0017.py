import calendar

while True:
    try:
        ano = int(input("Digite o ano que quer ver se é bissexto: "))

        if calendar.isleap(ano):
                print("É bissexto!")

        else:
                print("Não é bissexto!")
    except ValueError:
          print("Digite um valor valido!")