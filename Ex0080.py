nome_e_media = {}; 

nome_e_media['nome'] = str(input("Digite o nome do aluno: ")); 
nome_e_media['media'] = int(input("Digite a media no aluno: ")); 
        
for key, value in nome_e_media.items():
        print(f"\n{key} é igual á {value}"); 
 
if (nome_e_media["media"] > 5):
        print("\nAPROVADO!"); 
       
else:
        print(f"\nREPROVADO!"); 