# =============================================================================
# ARQUIVO: pilha_super_comentada.py
# OBJETIVO (para alunos ADS 2º semestre):
#   - Entender como funciona uma PILHA (Stack) usando ENCADEAMENTO (lista ligada).
#   - Treinar os métodos clássicos: push (empilhar), pop (desempilhar), peek (espiar),
#     isEmpty (verificar vazia).
#   - Perceber o comportamento LIFO (Last In, First Out = o último que entra é o
#     primeiro que sai).
#   - Ler cuidadosamente cada comentário e experimentar o código.
#
# DICA GERAL:
#   - Execute e LEIA a saída do console com calma.
#   - Mude valores e observe o que acontece (aprendizado ativo).
# =============================================================================


# =============================================================================
# AQUECIMENTO: PRIMEIROS PRINTS
# -----------------------------------------------------------------------------
# - Não têm relação direta com a pilha; servem apenas como "aquecimento" para
#   lembrar que o Python executa instruções de cima para baixo.
# - Você pode comentar esses prints quando não quiser vê-los.
# =============================================================================
print("hello world")   # 1ª vez
print("hello world")   # 2ª vez
print("hello world")   # 3ª vez


# =============================================================================
# PARTE 1 — CLASSE NODE (NÓ DA LISTA ENCADEADA)
# -----------------------------------------------------------------------------
# Por que precisamos de "Node"?
# - Nossa pilha será feita em cima de uma lista ligada (encadeada).
# - Cada elemento da pilha será um "nó" (Node) que guarda:
#     * valor (o dado do usuário)
#     * proximo (uma referência para o próximo nó abaixo dele)
#
# Visual (exemplo de 3 nós empilhados: topo=3):
#   topo ---> [valor=3 | proximo] ---> [valor=2 | proximo] ---> [valor=1 | None]
#                                                 (base)                    (fim)
#
# Observação:
# - Em Python, None é o "vazio" (equivalente ao null em outras linguagens).
# =============================================================================
class Node:
    # Definimos os ATRIBUTOS "padrão" do nó:
    valor = 0       # tipo típico: int (mas Python aceita outros tipos também)
    proximo = None  # tipo: Node (ou None quando for o último da cadeia)

    # Construtor do nó:
    # - valorParam: o dado a ser guardado (ex: número inteiro)
    # - proxNodeParam: o nó que vem logo abaixo (ou None, se não houver)
    def __init__(self, valorParam, proxNodeParam):
        # self.valor: guarda o dado do nó
        self.valor = valorParam
        # self.proximo: aponta para o próximo nó
        self.proximo = proxNodeParam

        # Importante:
        # - Não fazemos validação de tipo aqui para manter o exemplo simples.
        # - Em sistemas reais, poderíamos validar tipos ou negar valores inválidos.


# =============================================================================
# PARTE 2 — CLASSE STACK (PILHA)
# -----------------------------------------------------------------------------
# Sobre a pilha:
# - Estrutura LIFO (Last In, First Out): o último inserido é o primeiro removido.
# - Operações principais (todas O(1), custo constante, pois mexem só no topo):
#     * push(x): coloca x no TOPO.
#     * pop(): remove e retorna o valor do TOPO.
#     * peek(): retorna o valor do TOPO (sem remover).
#     * isEmpty(): diz se está vazia (True/False).
#
# Representação interna:
# - Guardamos apenas a referência do "topo" e um "tamanho".
# - Cada push liga o novo nó ao topo antigo e atualiza o topo.
# - Cada pop move o topo para o "próximo" nó da cadeia.
# =============================================================================
class Stack:
    # Atributos da pilha:
    topo = None     # referência para o Node do topo | None se vazia
    tamanho = 0     # quantidade de elementos na pilha

    # Construtor: inicia a pilha vazia
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    # -------------------------------------------------------------------------
    # MÉTODO: push(valorParam)
    # Função: empilhar um novo valor no topo da pilha.
    # Passo a passo:
    #   1) Criar um novo nó com o valor recebido.
    #   2) Apontar o "proximo" desse novo nó para o topo atual.
    #   3) Atualizar o topo para ser o novo nó.
    #   4) Aumentar o tamanho em +1.
    #
    # Custo: O(1)
    # Observação: Aceita valores repetidos (não verificamos duplicidade aqui).
    # -------------------------------------------------------------------------
    def push(self, valorParam):
        # 1) cria o novo nó com "valorParam" e, por enquanto, sem próximo
        novoNo = Node(valorParam, None)

        # 2) o próximo do novo nó passa a ser o topo atual
        #    (se a pilha estava vazia, self.topo é None, o que é ok)
        novoNo.proximo = self.topo

        # 3) atualiza o topo da pilha: agora o topo é o novo nó
        self.topo = novoNo

        # 4) ajusta a contagem de elementos
        self.tamanho += 1

    # -------------------------------------------------------------------------
    # MÉTODO: peek()
    # Função: ver o valor do topo SEM removê-lo da pilha.
    # Regras:
    #   - Se estiver vazia, avisamos e retornamos None.
    #   - Caso contrário, devolvemos self.topo.valor.
    #
    # Custo: O(1)
    # -------------------------------------------------------------------------
    def peek(self):
        if (self.isEmpty()):       # checa se a pilha está vazia
            print("Pilha vazia!")  # feedback amigável
            return None            # None significa "não há valor"
        else:
            return self.topo.valor

    # -------------------------------------------------------------------------
    # MÉTODO: pop()
    # Função: remover e retornar o valor do topo.
    # Passo a passo (se NÃO estiver vazia):
    #   1) Guardar o valor atual do topo (para retornar depois).
    #   2) Mover o topo para o próximo nó (topo = topo.proximo).
    #   3) Diminuir o tamanho em -1.
    #   4) Retornar o valor que estava no topo.
    #
    # Caso esteja vazia:
    #   - Avisar e retornar None.
    #
    # Custo: O(1)
    # -------------------------------------------------------------------------
    def pop(self):
        if (self.isEmpty()):
            print("Pilha vazia!!!")    # mensagens diferentes ajudam a ver
            return None                 # que realmente entrou nesse caso
        else:
            # 1) guarda o valor do topo para retornar
            valorDoTopo = self.topo.valor

            # 2) move o topo para o nó debaixo
            self.topo = self.topo.proximo

            # 3) diminui a contagem de elementos
            self.tamanho -= 1

            # 4) retorna o valor removido
            return valorDoTopo

    # -------------------------------------------------------------------------
    # MÉTODO: isEmpty()
    # Função: dizer se a pilha está vazia (True/False).
    # Regras:
    #   - Está vazia se o topo é None.
    #   - Caso contrário, não está vazia.
    #
    # Custo: O(1)
    # -------------------------------------------------------------------------
    def isEmpty(self):
        if (self.topo == None):
            return True
        else:
            return False


# =============================================================================
# PARTE 3 — "MAIN": BLOCOS DE TESTE
# -----------------------------------------------------------------------------
# Objetivo desta parte:
#   - Executar a pilha em cenários variados e observar o comportamento.
#   - Ler as mensagens e entender como os métodos funcionam na prática.
#
# Observação importante sobre "range" e pop():
#   - Quando fazemos: for i in range(pilha.tamanho):
#       * O range calcula a quantidade ANTES de o laço começar.
#       * Mesmo que pilha.tamanho diminua dentro do laço (por causa de pop()),
#         o "range" já está definido e o laço vai rodar aquele número de vezes.
# =============================================================================

# -----------------------------------------------------------------------------
# Bloco 1 — Estado inicial de duas pilhas vazias
# -----------------------------------------------------------------------------
pilha1 = Stack()
pilha2 = Stack()

# "topo" de uma pilha vazia é None
print(f"Valor do topo {pilha1.topo}")     # Deve aparecer "None"
print(f"Vazia?  {pilha1.isEmpty()}")      # Deve ser True


# -----------------------------------------------------------------------------
# Bloco 2 — Empilhando números de 1 a 100 em pilha1
# -----------------------------------------------------------------------------
for i in range(1, 101):    # 1, 2, 3, ..., 100
    pilha1.push(i)

# CUIDADO: imprimir "pilha1.topo" mostra o OBJETO Node (tipo e endereço),
# não o valor dentro dele. Para ver o valor, use peek().
print(f"Topo {pilha1.topo}")               # mostra algo como <__main__.Node object ...>
print(f"Valor do topo {pilha1.peek()}")    # deve ser 100 (último empilhado)
print(f"Vazia {pilha1.isEmpty()}")         # False (tem 100 elementos)

# -----------------------------------------------------------------------------
# Bloco 3 — Primeiros pops (removendo alguns elementos do topo)
# -----------------------------------------------------------------------------
print(f"Tamanho atual {pilha1.tamanho}")
print(f"Desempilhando {pilha1.pop()}")  # remove 100
print(f"Desempilhando {pilha1.pop()}")  # remove 99
print(f"Desempilhando {pilha1.pop()}")  # remove 98
print(f"Desempilhando {pilha1.pop()}")  # ...
print(f"Desempilhando {pilha1.pop()}")
print(f"Desempilhando {pilha1.pop()}")
print(f"Desempilhando {pilha1.pop()}")
print(f"Desempilhando {pilha1.pop()}")
print(f"Desempilhando {pilha1.pop()}")

print(f"Tamanho atual {pilha1.tamanho}")  # tamanho reduziu 9


# -----------------------------------------------------------------------------
# Bloco 4 — Esvaziando quase tudo (de propósito deixamos 1 no final)
# -----------------------------------------------------------------------------
# Observação:
#   - "range(pilha1.tamanho - 1)" pega um INSTANTÂNEO do tamanho atual
#     e vai desempilhar essa quantidade, deixando UM elemento na pilha.
#   - É intencional para testarmos o comportamento do peek() com 1 elemento.
for i in range(pilha1.tamanho - 1):
    print(f"Desempilhando {pilha1.pop()}")

print(f"Tamanho atual {pilha1.tamanho}")   # deve ser 1
print(f"Valor topo atual {pilha1.peek()}") # mostra o último que sobrou


# -----------------------------------------------------------------------------
# Bloco 5 — Reiniciando pilhas e praticando transferência de elementos
# -----------------------------------------------------------------------------
pilha1 = Stack()   # nova pilha1 vazia
pilha2 = Stack()   # nova pilha2 vazia

# Empilhando 1..10 em pilha1
for i in range(1, 11):
    pilha1.push(i)

print(f"Tamanho pilha1 {pilha1.tamanho}")      # 10
print(f"Valor topo pilha1 {pilha1.peek()}")    # 10

print(f"Tamanho pilha2 {pilha2.tamanho}")      # 0
print(f"Valor topo pilha2 {pilha2.peek()}")    # None + aviso "Pilha vazia!"

# Transferindo tudo de pilha1 para pilha2:
#   - Ao fazer pop() em pilha1 e push() em pilha2,
#     a ordem INVERTE (propriedade típica de duas pilhas).
#   - O "range(pilha1.tamanho)" captura a quantidade INICIAL (10),
#     e mesmo reduzindo durante os pops, o laço rodará 10 vezes.
for i in range(pilha1.tamanho):
    valorTemp = pilha1.pop()   # remove do topo de pilha1 (10, 9, 8, ...)
    pilha2.push(valorTemp)     # empilha em pilha2 (fica 10 no topo, depois 9, etc.)
    print(f"Valor desempilhado1 {valorTemp}")

print(f"Tamanho pilha1 {pilha1.tamanho}")      # 0
print(f"Valor topo pilha1 {pilha1.peek()}")    # None + aviso

print(f"Tamanho pilha2 {pilha2.tamanho}")      # 10
print(f"Valor topo pilha2 {pilha2.peek()}")    # 1 ou 10? Pense!
# Dica: como empilhamos em pilha2 na sequência 10,9,8,..., o TOPO final é 1? Não!
#       Veja: primeiro push(10) -> topo=10; depois push(9) -> topo=9; ... no fim, topo=1.
#       Logo, peek() aqui deve mostrar 1.

# Esvaziando pilha2 completamente
for i in range(pilha2.tamanho):
    print(f"Desempilhando {pilha2.pop()}")   # imprime 1, 2, 3, ..., 10 (ordem crescente)

# FIM — Volte e refaça alguns blocos mudando valores para testar seu entendimento.
