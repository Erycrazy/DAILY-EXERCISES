#Verificador de voto opcional, obrigatorio, não vota

def voto(ano_nascimento):
    idade = 2025 - ano_nascimento
    
    if (16 <= idade < 18):
        return print(f"Com {idade} anos - VOTO OPCIONAL"); 
    
    elif (idade < 16):
        return print(f"Com {idade} anos - NÃO VOTA"); 
    
    elif (18 <= idade <= 59):
        return print(f"Com {idade} anos - VOTO OBRIGATORIO"); 
    
    else:
        return print(f"Com {idade} anos - VOTO OPCIONAL!"); 
    
nascimento_usuario = int(input("Digite sua data de nascimento: ")); 

voto(nascimento_usuario); 