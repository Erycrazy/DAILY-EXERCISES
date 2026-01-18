transporte = str(input("Digite: "));

match transporte:
    case "carro":
        print("Veiculo Terrestre!");
        
    case "avião":
        print("Veiculo Aereo!");
        
    case "barco":
        print("Veiculo marinho!");
        
    case _:
        print("Nãi indentificado!");