def cadastrarPessoas(arq, nome = 'desconhecido', idade = 0):
    try:
        a = open(arq, 'at'); 
        
    except:
        print("Houve um ERRO na abertura do arquivo!"); 
        
    else: 
        try:
            a.write(f'{"="*50}\nNOME: {nome}\nIDADE: {idade}\n{"="*50}\n'); 
        except:
            print("Houve um ERRO na hora de escrever os dados!"); 
            
        else: 
            print(f"Novo registro de {nome} adicionado!"); 

def arquivoExiste(nome):
    try:
        arquivo = open(nome, 'rt'); 
        arquivo.close(); 
        
    except FileNotFoundError:
        return False; 
    else:
        return True; 
    
def criarArquivo(nome):
    try:
        arquivo = open(nome, 'wt+'); #Esse + serve para caso não aja um arquivo ele cria
        arquivo.close(); 
        
    except:
        print("Houve um ERRO na criação de arquivo!"); 
        
    else:
        print("Arquivo criado com sucesso!"); 
         
def listarPessoas(nome):
    try:
        a = open(nome, "rt"); 
    
    except:
        print("Erro ao ler o arquivo!"); 
        
    else:
        print(f"{"="*16} LISTA DE PESSOAS {"="*16}"); 
        print(a.read()); 
    
    finally:
        a.close(); 
        
def menuPrincipal():
    while True:
        print("===== MENU PRINCIPAL ====="); 
        print("1 - CADASTRAR PESSOAS"); 
        print("2 - LISTAR PESSOAS"); 
        print("3 - SAIR\n"); 
    
        try:
            opcao = int(input("Escolha uma opção: ")); 
            match (opcao):
                case 1:
                    nome = input("Digite o nome: "); 
                    idade = int(input("Digite a idade: ")); 
                    cadastrarPessoas(arq, nome, idade); 
                    continue; 
                
                case 2:
                    listarPessoas(arq); 
                    continue; 
                                
                case 3:
                    print("Saindo..."); 
                    break; 
                
                case _:
                    print("Opção invalida!"); 
                
        except(ValueError, TypeError):
            print(f"Valor invalido!"); 
            continue; 
        
arq = "arquivo.txt"

if (not arquivoExiste(arq)):
    criarArquivo(arq); 
        
menuPrincipal(); 