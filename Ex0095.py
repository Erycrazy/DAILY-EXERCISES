def leiaInt(mensagemParam):
    while True:
        try: 
            valor01 = int(input(mensagemParam));  
        
        except (ValueError, TypeError):
            print("Você não digitou um numero inteiro!"); 
            continue; 
        
        except (KeyboardInterrupt):
            print("O usuario prefiriu não digitar o numero..."); 
            return 0 ; 
        
        else:
            print(f"O valor Real foi {valor01}"); 
            break; 
        
          
def leiaFloat(mensagemParam):
    while True:
        try:
            valor02 = float(input(mensagemParam)); 
             
        except (ValueError, TypeError):
            print("Você não digitou um numero Real!"); 
            continue; 
            
        except (KeyboardInterrupt):
            print("O usuario prefiriu não digitar o numero..."); 
            return 0; 
              
        else:
            print(f"O valor Real foi {valor02}"); 
            break; 

        
leiaInt("Digite um valor: "); 
leiaFloat("Digite outro valor: "); 

    
        