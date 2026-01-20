#Calcular a Area

def area(larguraParam, comprimentoParam):
    area = (larguraParam * comprimentoParam); 
    return print(f"A area é: {area}m²"); 

#Codigo Principal
largura = float(input("Digite a largura: ")); 
comprimento = float(input("Digite o comprimento: ")); 

area(largura, comprimento); 