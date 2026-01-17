menu = int(input("1 - Pizza\n2 - Sushi\n3 - Salada\n\nDigite a opção que quer: "));

match menu:
    case 1:
        print("Você escolheu Pizza");
        
    case 2:
        print("Você escolheu Sushi");

    case 3:
        print("Você escolheu Salada");
        
    case _:
        print("Opção invalida!");
        