from random import randint; 

numeros = []; 
soma_num = []; 

def sorteia():
    for i in range(5):
        numeros.append(randint(1, 5)); 
    return print(f"Os numeros da lista é: {numeros}"); 
      
def somaPar():
    for valor in numeros:
        if (valor % 2 == 0):
            soma_num.append(valor); 
            
    return sum(soma_num); 

sorteia(); 
print(f"A soma dos numeros pares é: {somaPar()}"); 