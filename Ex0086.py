from time import sleep; 

def contador(inicioParam, fimParam, passoParam):
    for valorParam in range(inicioParam, fimParam, passoParam):
        print(f"{valorParam}", end=" "); 
        sleep(0.5); 

        
inicio = int(input("Quanto numeros você quer: ")); 
fim = int(input("Até aonde esse numero vai?: ")); 
passo = int(input("De quanto em quanto vai: ")); 

contador(inicioParam=inicio, fimParam=fim, passoParam=passo); 