def ficha(nomeParam, golsParam):
    nomeParam = ["ronaldo", "ronaldinho", "cr7", "pele"]; 
    
    if  "ronaldo" in nomeParam:
        return print(f"O Jogador {nomeParam[0]}, marcou {golsParam} gols!"); 
    
    elif "ronaldinho" in nomeParam:
        return print(f"O Jogador {nomeParam[1]}, marcou {golsParam} gols!"); 
    
    elif "cr7" in nomeParam:
        return print(f"O Jogador {nomeParam[2]}, marcou {golsParam} gols!"); 
    
    elif "pele" in nomeParam:
        return print(f"O Jogador {nomeParam[3]}, marcou {golsParam} gols!"); 
    
    else:
        return print(f"O Jogador <desconhecido>, marcou 0 gols!"); 
    
nome = str(input("Digite o nome do jogador: ")); 
gols = int(input("Digite quantos gols ele marcou: ")); 

print(ficha(nome, gols)); 
    