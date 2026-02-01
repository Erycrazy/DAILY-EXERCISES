def fatorial(numero, show):
    resultado = 1; 
    for i in range(1, numero + 1):
        resultado *= i; 
    if (show == False):
        return resultado; 
    
    elif (show == True):
        while numero <= 1:
            mostre = print(f"{numero} X {numero - 1}"); 
        return mostre;    
    
    
    
print(fatorial(5, show=True));      
