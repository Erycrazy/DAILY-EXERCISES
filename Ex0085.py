# ===================== VARIÁVEIS SIMPLES (strings e inteiros) =====================

nome = "yuri"                             # string: sequência de caracteres (texto)
email = "yuri.padua@prof.unip.br"         # outra string
id = 123456                               # inteiro (int)
# OBS pedagógica: "id" também é o nome de uma função interna do Python (id()).
# Aqui está tudo bem, mas em projetos maiores é melhor evitar sobrescrever nomes "famosos".

# ===================== LISTA (ARRAY) HETEROGÊNEA =====================
# Abaixo há um exemplo de lista com tipos misturados (strings, números, referência a variável).
# Em Python, listas podem misturar tipos, mas na prática é melhor manter a lista com um tipo só
# para evitar confusão (ex.: lista só de notas, ou só de nomes).
#
# A lista está comentada porque você quis manter como exemplo didático.
# Logo abaixo, há 3 formas diferentes de percorrer/imprimir a lista (for com índice, while e for-in).
# Mantive TUDO como estava (comentado) e acrescentei comentários explicativos.

# listaFrutas = ['maça',
#                2,
#                'banana',
#                 'pera',
#                 3.14,
#                  'uva',
#                  nome,              
#                  'pitanga']

# print(listaFrutas)  # imprime a lista inteira de uma vez

# print("IMPRIMINDO NO FOR")
# for i in range(len(listaFrutas)):      # range( len(listaFrutas) ) -> 0 até último índice
#     item = listaFrutas[i]              # acessa por índice
#     print(f"item {i} = {item}")        # mostra posição e valor


# print("IMPRIMINDO NO WHILE")
# count = 0
# while (count < len(listaFrutas)):                      # repete enquanto count for um índice válido
#     print(f"item {count} = {listaFrutas[count]}")      # acessa por índice
#     count += 1                                         # incrementa (evita loop infinito)


# print("IMPRIMINDO NO FOR-IN")
# for item in listaFrutas:                # percorre direto os valores (sem usar índice)
#     print(f"item = {item}") 


# # print("IMPRIMINDO NO FOR-IN")
# # for pos,item in enumerate(listaFrutas):  # enumerate devolve (posição, valor)
# #     print(f"item {pos} = {item}") 


# ===================== OPERAÇÕES COM LISTA: EXEMPLO COM NOTAS =====================

print("DAQUI PARA BAIXO OPERAÇÕES COM LISTA")

listaNotas = []  # lista vazia (boa prática: manter um único tipo: float para notas)

# Abaixo, os exemplos estão comentados para fins didáticos.
# Eles mostram várias formas de:
# 1) Inserir na lista (append),
# 2) Somar valores (sum),
# 3) Calcular média (dividindo pela quantidade de elementos com len(listaNotas)),
# 4) Percorrer a lista com for e range (usando índices).
#
# DICAS:
# - Sempre converta input para float ao trabalhar com notas.
# - Antes de dividir por len(listaNotas), garanta que a lista NÃO está vazia (len > 0),
#   senão ocorre ZeroDivisionError.

# print(listaNotas)
# listaNotas.append(float(input("Digite a nota 1: ")))  # append: adiciona no fim da lista
# listaNotas.append(float(input("Digite a nota 2: ")))
# listaNotas.append(float(input("Digite a nota 3: ")))
# print(listaNotas)

# soma = sum(listaNotas)                      # sum: soma todos os itens da lista (numéricos)
# media = soma / len(listaNotas)              # len: quantidade de itens
# print(f"A soma das notas é {soma} e a média é {media}") 

# soma = 0
# for i in range(len(listaNotas)):            # modo "manual": somar elemento por elemento
#     soma += listaNotas[i]
#     print(f"Nota {i+1} = {listaNotas[i]}")  # imprime cada nota com seu número "humano" (i+1)
# print(f"A soma das notas é {soma} e a média é {soma/len(listaNotas)}")


# print(f"AGORA UM EXEMPLO COM NÚMERO VARIÁVEL DE NOTAS")
# numNotas = int(input("Quantas notas você quer inserir? "))
# listaNotas2 = []                             # nova lista para este exemplo
# for i in range(numNotas):
#     listaNotas2.append(float(input(f"Digite a nota {i+1}: ")))
# suma2 = sum(listaNotas2)                     # note que aqui no original está 'suma2' (sem 'o').
# media2 = suma2 / len(listaNotas2)   
# print(f"A soma das notas é {suma2} e a média é {media2}")


# ===================== INTRODUÇÃO BÁSICA À POO (CLASSE PESSOA) =====================

print("AGORA UM EXEMPLO COM CLASSE PESSOA")

# Classe = "molde" que descreve como os objetos serão (atributos) e o que podem fazer (métodos).
# Abaixo, definimos atributos simples e um método apresentar() para "falar" os dados da pessoa.
# OBS importante sobre listas em classes:
#   - Colocar 'listaNotas = []' no nível da classe cria um ATRIBUTO DE CLASSE (compartilhado).
#   - Dentro do __init__, fazemos 'self.listaNotas = []', que é ATRIBUTO DE INSTÂNCIA (individual).
#   - Isso evita que várias pessoas compartilhem a mesma lista acidentalmente (o que seria ruim).
class Pessoa:
    # ATRIBUTOS DE CLASSE (valores padrão/descrição): evite usar mutáveis aqui em projetos reais
    nome = ""
    idade = 0
    cpf = ""
    rg = ""
    email = ""
    listaNotas = []  # cuidado: mutável no nível da classe (ainda bem que vamos sobrescrever no __init__)

    def __init__(self, nome, idade, cpf, rg, email):
        # __init__ é o "construtor": executa ao criar o objeto
        # self = referência ao OBJETO específico que está sendo criado
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.rg = rg
        self.email = email
        self.listaNotas = []  # ATRIBUTO DE INSTÂNCIA (cada pessoa terá sua própria lista)

    def apresentar(self):
        # Método de instância: usa self para acessar os dados da própria pessoa.
        # Aqui, o método APENAS imprime e NÃO retorna nada (retorno padrão é None).
        print(
            f"Olá, meu nome é {self.nome}, tenho {self.idade} anos, "
            f"meu cpf é {self.cpf}, meu rg é {self.rg} e meu email é {self.email}"
        )
        # Não há 'return' aqui → retorno é None (isso é relevante lá embaixo quando usamos print(...))



# Abaixo, exemplo de FUNÇÃO comum (fora da classe) com parâmetros nomeados:
# Mantive tudo comentado como no original e acrescentei explicações.
# def seuNomeEdoCachorro(nomeDoUsuarioEspecial, doginho):
#     print(f"Seu nome é {nomeDoUsuarioEspecial} e o nome do seu cachorro é {doginho}")

# seuNomeEdoCachorro(nomeDoUsuarioEspecial="Yuri", doginho="Rex")     # chamada com argumentos nomeados
# seuNomeEdoCachorro(doginho="Totó", nomeDoUsuarioEspecial="João")    # ordem não importa quando nomeados


# ===================== CRIAÇÃO DO OBJETO E USO DOS MÉTODOS/ATRIBUTOS =====================

len(listaNotas)  # Esta linha apenas calcula o tamanho da lista, mas NÃO faz nada com o resultado.
                 # Se quisermos ver o valor, precisaríamos: print(len(listaNotas)) ou guardar em uma variável.

nome = 'Yuri'
pessoa1 = Pessoa(                      # cria um objeto (instância) da classe Pessoa
    nome=nome,                         # argumentos NOMEADOS: muito legíveis e fáceis de entender
    idade=44,
    cpf='123.456.789-00',
    rg='12.345.678-9',
    email='yuri@prof',
)

print(pessoa1.nome)                    # acessa um ATRIBUTO de instância
print(pessoa1.apresentar())            # cuidado: apresentar() imprime e retorna None.
                                       # Então isso vai imprimir a apresentação e, depois, imprimir "None".

# Inserindo notas na lista da pessoa (lista do OBJETO, não a do nível da classe):
pessoa1.listaNotas.append(8.5)         # append adiciona no fim
pessoa1.listaNotas.append(7.0)
print(pessoa1.listaNotas)              # mostra a lista de notas da pessoa (ex.: [8.5, 7.0])

print(pessoa1.apresentar())            # de novo: imprime a apresentação e depois imprime "None"
                                       # (se quiser evitar imprimir "None", use apenas: pessoa1.apresentar())

# DICA (opcional, apenas para estudo, mantendo o espírito do arquivo):
# Para calcular média das notas da pessoa, poderíamos (em outra aula) fazer:
if len(pessoa1.listaNotas) > 0:
    media = sum(pessoa1.listaNotas) / len(pessoa1.listaNotas)
    print(f"Média de {pessoa1.nome} = {media}")
else:
    print("Sem notas cadastradas ainda.")   