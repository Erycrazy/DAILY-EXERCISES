# type: ignore
import random as Random

# =============================================================================
# ESTRUTURA DE DADOS: LISTA ENCADEADA EM PYTHON
# -----------------------------------------------------------------------------
# - Implementaremos uma LISTA encadeada com nos (Node), mantendo ponteiros
#   para o INICIO (cabeca) e para o FIM (cauda) da lista.
# - Usaremos nomes de metodos comuns em E.D. classica:
#     push, pop, remove, clear, is_empty, size, get, set, insert, pop_at
# - Teremos tambem alguns "extras" uteis para a pratica:
#     push_front, pop_front, front, back, peek, __len__, __repr__
#
# O QUE E UMA LISTA ENCADEADA?
# - E uma sequencia de nos; cada no aponta para o proximo.
# - Diferente de listas nativas do Python (list), aqui controlamos manualmente
#   as ligacoes (ponteiros) entre os nos.
# - Vantagem: insercoes/remocoes no comeco O(1).
# - Desvantagem: acessar por indice e O(n) (precisamos percorrer).
#
# DECISOES DE PROJETO NESTE ARQUIVO:
# - Usaremos LISTA ENCADEADA SIMPLES (apenas "proximo").
# - Guardaremos ponteiros para:
#     _inicio  -> primeiro no
#     _fim     -> ultimo no
#   Isso torna push (inserir no fim) O(1).
# - O pop (remover do fim) em lista simples e O(n), pois precisamos achar
#   o "penultimo" no percorrendo a lista.
# =============================================================================


# =============================================================================
# PARTE 1 — CLASSE Node (no da lista)
# -----------------------------------------------------------------------------
# Cada NO guarda:
# - valor: dado (qualquer tipo)
# - proximo: referencia para o proximo no (ou None, se for o ultimo)
# =============================================================================
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


# =============================================================================
# PARTE 2 — CLASSE Lista (lista encadeada simples)
# -----------------------------------------------------------------------------
# ATRIBUTOS PRINCIPAIS:
# - _inicio: referencia para o primeiro no
# - _fim:    referencia para o ultimo no
# - _tamanho: quantidade de elementos
#
# METODOS CLASSICOS (nomes de E.D.):
# - push(valor):   insere no FIM da lista (como em arrays dinamicos)
# - pop():         remove e retorna o ULTIMO elemento (erro se vazia)
# - remove(valor): remove a PRIMEIRA ocorrencia do valor (se existir)
# - clear():       esvazia a lista (limpa tudo)
# - is_empty():    True/False se esta vazia
# - size():        retorna quantidade de elementos
#
# METODOS COMPLEMENTARES MUITO UTEIS:
# - push_front(valor): insere no INICIO (cabeca)
# - pop_front():       remove do INICIO
# - get(i):            retorna o valor no indice i
# - set(i, valor):     altera o valor no indice i
# - insert(i, valor):  insere ANTES do indice i
# - pop_at(i):         remove e retorna o valor no indice i
# - front():           ve o primeiro (sem remover)
# - back() / peek():   ve o ultimo (sem remover)
# - __len__():         integra com len(lista_obj)
# - __repr__():        imprime de forma amigavel para debug
# =============================================================================
class Lista:
    def __init__(self):
        # lista comeca vazia
        self._inicio = None
        self._fim = None
        self._tamanho = 0

    # -------------------------------------------------------------------------
    # push(valor) — INSERE NO FIM (O(1))
    # -------------------------------------------------------------------------
    def push(self, valor):
        novo = Node(valor)

        if self.is_empty():
            # Se estava vazia, INICIO e FIM apontam para o novo no
            self._inicio = novo
            self._fim = novo
        else:
            # Liga o antigo FIM ao novo no e atualiza o ponteiro _fim
            self._fim.proximo = novo
            self._fim = novo

        self._tamanho += 1

    # -------------------------------------------------------------------------
    # pop() — REMOVE DO FIM E RETORNA O VALOR (O(n) em lista simples)
    # - Se vazia -> IndexError (underflow)
    # - Caso 1: apenas 1 elemento -> zera INICIO e FIM
    # - Caso 2: >1 elemento -> percorre ate o penultimo e ajusta FIM
    # -------------------------------------------------------------------------
    def pop(self):
        if self.is_empty():
            raise IndexError("Nao e possivel pop(): a lista esta vazia (underflow).")

        # Caso com 1 elemento
        if self._inicio is self._fim:
            valor = self._inicio.valor
            self._inicio = None
            self._fim = None
            self._tamanho = 0
            return valor

        # Caso com 2 ou mais: precisamos achar o penultimo no
        penultimo = self._inicio
        ultimo = self._inicio.proximo
        while ultimo is not self._fim:
            penultimo = ultimo
            ultimo = ultimo.proximo

        # 'atual' esta no FIM, 'anterior' e o penultimo
        valor = self._fim.valor
        penultimo.proximo = None
        self._fim = penultimo
        self._tamanho -= 1
        return valor

    # -------------------------------------------------------------------------
    # remove(valor) — REMOVE A PRIMEIRA OCORRENCIA (se existir) e retorna True.
    # Se nao achar, retorna False. Complexidade: O(n).
    # -------------------------------------------------------------------------
    def remove(self, valor):
        if self.is_empty():
            return False

        # Caso 1: o valor esta logo no INICIO
        if self._inicio.valor == valor:
            self.pop_front()
            return True

        # Caso 2: valor pode estar no meio ou no fim
        anterior = self._inicio
        atual = self._inicio.proximo
        while atual is not None:
            if atual.valor == valor:
                # "Pula" o 'atual' (remocao)
                anterior.proximo = atual.proximo
                # Se o removido era o FIM, atualiza ponteiro _fim
                if atual is self._fim:
                    self._fim = anterior
                self._tamanho -= 1
                return True
            anterior = atual
            atual = atual.proximo

        return False  # nao encontrou

    # -------------------------------------------------------------------------
    # clear() — esvazia a lista rapidamente (O(1))
    # -------------------------------------------------------------------------
    def clear(self):
        self._inicio = None
        self._fim = None
        self._tamanho = 0

    # -------------------------------------------------------------------------
    # is_empty() — True/False se a lista esta vazia
    # -------------------------------------------------------------------------
    def is_empty(self) -> bool:
        return self._inicio is None

    # -------------------------------------------------------------------------
    # size() — retorna quantidade de elementos (O(1))
    # -------------------------------------------------------------------------
    def size(self) -> int:
        return self._tamanho

    # ========================= METODOS COMPLEMENTARES ========================

    # -------------------------------------------------------------------------
    # push_front(valor) — INSERE NO INICIO (O(1))
    #   Util para mostrar a vantagem da lista encadeada nesta operacao.
    # -------------------------------------------------------------------------
    def push_front(self, valor):
        novo = Node(valor)
        if self.is_empty():
            self._inicio = novo
            self._fim = novo
        else:
            novo.proximo = self._inicio
            self._inicio = novo
        self._tamanho += 1

    # -------------------------------------------------------------------------
    # pop_front() — REMOVE DO INICIO E RETORNA O VALOR (O(1))
    #   Se vazia -> IndexError.
    # -------------------------------------------------------------------------
    def pop_front(self):
        if self.is_empty():
            raise IndexError("Nao e possivel pop_front(): a lista esta vazia.")

        valor = self._inicio.valor
        self._inicio = self._inicio.proximo
        # Se esvaziou, ajusta _fim tambem
        if self._inicio is None:
            self._fim = None
        self._tamanho -= 1
        return valor

    # -------------------------------------------------------------------------
    # get(i) — RETORNA o valor no indice i (0-based). O(n).
    #   - Se i for invalido (fora de 0..size-1), IndexError.
    # -------------------------------------------------------------------------
    def get(self, indice: int):
        self._validar_indice_acesso(indice)
        atual = self._inicio
        pos = 0
        while pos < indice:
            atual = atual.proximo
            pos += 1
        return atual.valor

    # -------------------------------------------------------------------------
    # set(i, valor) — ALTERA o valor no indice i (0-based). O(n).
    #   - Se i for invalido, IndexError.
    # -------------------------------------------------------------------------
    def set(self, indice: int, valor):
        self._validar_indice_acesso(indice)
        atual = self._inicio
        pos = 0
        while pos < indice:
            atual = atual.proximo
            pos += 1
        atual.valor = valor

    # -------------------------------------------------------------------------
    # insert(i, valor) — INSERE ANTES do indice i (0-based). O(n).
    #   Regras:
    #     * i == 0            -> push_front(valor)
    #     * i == size()       -> push(valor) (insere no fim)
    #     * 0 < i < size()    -> insere no meio
    #     * caso contrario    -> IndexError
    # -------------------------------------------------------------------------
    def insert(self, indice: int, valor):
        if indice < 0 or indice > self._tamanho:
            raise IndexError(f"Indice invalido em insert(): {indice}")

        if indice == 0:
            self.push_front(valor)
            return
        if indice == self._tamanho:
            self.push(valor)
            return

        # Insercao no meio: precisamos chegar ao no anterior a posicao 'indice'
        anterior = self._inicio
        pos = 0
        while pos < (indice - 1):
            anterior = anterior.proximo
            pos += 1

        novo = Node(valor)
        novo.proximo = anterior.proximo
        anterior.proximo = novo
        self._tamanho += 1

    # -------------------------------------------------------------------------
    # pop_at(i) — REMOVE E RETORNA o valor no indice i (0-based). O(n).
    #   - i == 0         -> pop_front()
    #   - i == size()-1  -> pop()
    #   - meio           -> percorre, ajusta ligacoes
    # -------------------------------------------------------------------------
    def pop_at(self, indice: int):
        self._validar_indice_acesso(indice)

        if indice == 0:
            return self.pop_front()
        if indice == self._tamanho - 1:
            return self.pop()

        # Remocao no meio: achar anterior ao indice
        anterior = self._inicio
        pos = 0
        while pos < (indice - 1):
            anterior = anterior.proximo
            pos += 1

        atual = anterior.proximo
        valor = atual.valor
        anterior.proximo = atual.proximo
        self._tamanho -= 1
        return valor

    # -------------------------------------------------------------------------
    # front() — ve o PRIMEIRO elemento (sem remover). O(1).
    # back()  — ve o ULTIMO  elemento (sem remover). O(1).
    # peek()  — alias para back() (padrao comum em "pilhas/listas").
    # -------------------------------------------------------------------------
    def front(self):
        if self.is_empty():
            raise IndexError("front(): lista vazia.")
        return self._inicio.valor

    def back(self):
        if self.is_empty():
            raise IndexError("back(): lista vazia.")
        return self._fim.valor

    def peek(self):
        # Por convencao aqui, peek() retorna o ultimo (igual ao back()).
        return self.back()

    # -------------------------------------------------------------------------
    # Funcoes internas de apoio (validacao e representacao)
    # -------------------------------------------------------------------------
    def _validar_indice_acesso(self, indice: int):
        if indice < 0 or indice >= self._tamanho:
            raise IndexError(f"Indice invalido: {indice} (tamanho atual = {self._tamanho})")

    def __len__(self):
        return self._tamanho

    def __repr__(self) -> str:
        elementos = []
        atual = self._inicio
        while atual is not None:
            elementos.append(atual.valor)
            atual = atual.proximo

        if not elementos:
            return "Lista([])"
        return f"Lista({elementos})"


# =============================================================================
# PARTE 3 — Funcao auxiliar para IMPRESSAO didatica no console
# -----------------------------------------------------------------------------
# Imprime a lista do INICIO ate o FIM, desenhando setas para facilitar a leitura.
# =============================================================================
def imprimir_lista(lst: Lista):
    print("\n--- ESTADO ATUAL DA LISTA (inicio -> ... -> fim) ---")
    if lst.is_empty():
        print("[LISTA VAZIA]")
        print("---------------------------------------------------\n")
        return

    atual = lst._inicio
    while atual is not None:
        if atual.proximo is None:
            print(f"[{atual.valor}]  <-- FIM")
        else:
            print(f"[{atual.valor}] -> ", end="")
        atual = atual.proximo
    print("---------------------------------------------------\n")


# =============================================================================
# PARTE 4 — MAIN: testes passo a passo
# -----------------------------------------------------------------------------
# Execute este arquivo (python lista_encadeada.py) para acompanhar os testes.
# Leia as mensagens do console e confira se o comportamento esta correto.
# =============================================================================
def main():
    print("1) Criando uma lista vazia...")
    lista = Lista()
    imprimir_lista(lista)

    print("2) push(10), push(20), push(30)  -> insere NO FIM")
    lista.push(10)
    lista.push(20)
    lista.push(30)
    imprimir_lista(lista)

    print("3) push_front(5)  -> insere NO INICIO")
    lista.push_front(5)
    imprimir_lista(lista)

    print("4) front() e back()/peek() (sem remover)")
    try:
        print("front() =>", lista.front(), " (esperado 5)")
        print("back()  =>", lista.back(),  " (esperado 30)")
        print("peek()  =>", lista.peek(),  " (esperado 30)\n")
    except IndexError as e:
        print("Erro:", e, "\n")

    print("5) size() e is_empty()")
    print("size() =>", lista.size(), " (esperado 4)")
    print("is_empty() =>", lista.is_empty(), " (esperado False)\n")

    print("6) get(2)  -> deve retornar o terceiro elemento (indice 2)")
    try:
        print("get(2) =>", lista.get(2), " (esperado 20)\n")
    except IndexError as e:
        print("Erro:", e, "\n")

    print("7) set(1, 99) -> altera o valor do indice 1 (onde estava 10)")
    try:
        lista.set(1, 99)
        imprimir_lista(lista)
    except IndexError as e:
        print("Erro:", e, "\n")

    print("8) insert(2, 777) -> insere ANTES do indice 2")
    try:
        lista.insert(2, 777)
        imprimir_lista(lista)
    except IndexError as e:
        print("Erro:", e, "\n")

    print("9) pop_at(3) -> remove o elemento no indice 3 e retorna o valor")
    try:
        removido = lista.pop_at(3)
        print("pop_at(3) =>", removido)
        imprimir_lista(lista)
    except IndexError as e:
        print("Erro:", e, "\n")

    print("10) remove(30) -> remove a PRIMEIRA ocorrencia do valor 30")
    ok = lista.remove(30)
    print("remove(30) =>", ok, " (esperado True)")
    imprimir_lista(lista)

    print("11) pop() -> remove do FIM (esperado remover o ultimo restante)")
    try:
        print("pop() =>", lista.pop())
        imprimir_lista(lista)
    except IndexError as e:
        print("Erro:", e, "\n")

    print("12) pop_front() -> remove do INICIO")
    try:
        print("pop_front() =>", lista.pop_front())
        imprimir_lista(lista)
    except IndexError as e:
        print("Erro:", e, "\n")

    print("13) clear() -> esvazia a lista")
    lista.clear()
    imprimir_lista(lista)

    print("14) Teste de erro: pop() em lista vazia")
    try:
        lista.pop()
    except IndexError as e:
        print("Como esperado, deu erro no pop() com lista vazia:")
        print("->", e)

    print("\nOK! Lista encadeada (com metodos classicos) concluida!")


# =============================================================================
# *** SECAO EXTRA NO FINAL DO ARQUIVO ***
# BUBBLE SORT PARA ARRAYS (listas Python)
# -----------------------------------------------------------------------------
# Objetivo: mostrar a versao classica do Bubble Sort quando a estrutura
# e um ARRAY (list do Python), onde o acesso por indice e O(1).
# Essa implementacao NAO usa a Lista encadeada acima.
# =============================================================================

def bubble_sort_array(arr, verbose=False):
    """
    BUBBLE SORT (super simples, sem otimizacoes, ORDEM CRESCENTE)

    Ideia geral (explicacao para alunos):
    - Vamos "varrer" o array varias vezes.
    - Em cada varredura, comparamos pares de elementos ADJACENTES:
        arr[j] e arr[j+1]
    - Se estiverem fora de ordem (arr[j] > arr[j+1]), fazemos a TROCA.
    - Repetimos isso por (n-1) passadas completas.
    - Ao final, o array fica em ordem crescente.

    Parametros:
      - arr: lista Python (array) que sera ordenada "in place" (modificada)
      - verbose: se True, imprime cada comparacao e o estado do array

    Retorno:
      - o proprio arr (ja ordenado)
    """
    tamanho = len(arr)

    # Se tiver 0 ou 1 elemento, ja esta "ordenado"
    if tamanho <= 1:
        if verbose:
            print("Array com 0 ou 1 elemento. Nao ha o que ordenar.")
        return arr

    if verbose:
        print("\n==== INICIO DO BUBBLE SORT (crescente, sem otimizacoes) ====")
        print(f"Array inicial: {arr}\n")

    # Faremos (tamanho - 1) passadas completas
    for indice_passada in range(tamanho - 1):
        if verbose:
            print(f"--- Passada {indice_passada + 1} de {tamanho - 1} ---")

        # Em cada passada, comparamos TODAS as posicoes adjacentes j e j+1
        # (ate o final, sem encurtar)
        for indice_posicao in range(0, tamanho - 1):
            elemento_atual = arr[indice_posicao]
            proximo_elemento = arr[indice_posicao + 1]

            if verbose:
                print(f"Comparando posicoes {indice_posicao} e {indice_posicao + 1}: "
                      f"{elemento_atual} e {proximo_elemento}")

            # Se estiver fora de ordem (ex.: 8 antes de 3), trocamos
            if elemento_atual > proximo_elemento:
                if verbose:
                    print(" -> Fora de ordem! TROCANDO os dois.")

                # TROCA usando variavel temporaria (forma mais didatica)
                temporario = arr[indice_posicao]
                arr[indice_posicao] = arr[indice_posicao + 1]
                arr[indice_posicao + 1] = temporario
            else:
                if verbose:
                    print(" -> Ordem ok. NAO troca.")

            if verbose:
                print(f"Estado atual do array: {arr}\n")

        if verbose:
            print(f"Fim da passada {indice_passada + 1}. Array ate agora: {arr}")
            print("-" * 60)

    if verbose:
        print("\n==== FIM DO BUBBLE SORT ====")
        print(f"Array final ORDENADO: {arr}\n")

    return arr


def demo_bubble_sort_array():
    """
    DEMO SUPER SIMPLES (nao roda sozinha; chame manualmente)
    Objetivo: mostrar o bubble sort passo a passo com prints.
    """
    print("\n=== DEMO BUBBLE SORT PARA ARRAYS (SIMPLES) ===")
    dados = [38, 27, 43, 3, 9, 82, 10]
    print("ANTES (crescente):", dados)
    bubble_sort_array(dados, verbose=True)  # com verbose para ver todos os passos
    print("DEPOIS (crescente):", dados)



# =============================================================================
# PONTO DE ENTRADA
# -----------------------------------------------------------------------------
# Observacao: por padrao chamamos apenas main().
# Se quiser testar o bubble sort de array rapido, chame manualmente:
#   demo_bubble_sort_array()
# (veja instrucoes detalhadas apos o codigo)
# =============================================================================
if __name__ == "__main__":
    # main()          # corrigido: antes estava main2()
    demo_bubble_sort_array()  # OPCIONAL: descomente para ver o bubble em acao






# Lista de exercicios 

# Construcao basica
# Crie uma lista encadeada vazia, insira 5 numeros com push e mostre o estado usando imprimir_lista.

# Insercao no inicio
# Use push_front para inserir dois valores no inicio e confirme com front() que o primeiro elemento e o esperado.

# Acesso e alteracao
# Insira os valores [10, 20, 30, 40]. Use get(2) para ler o terceiro elemento e depois set(2, 99) para altera-lo. Mostre a lista antes e depois.

# Inserir no meio
# Com uma lista [5, 15, 25, 35], use insert(2, 999) para inserir antes do indice 2. Mostre o resultado e explique o que aconteceu com os ponteiros.

# Remocao por valor
# Dada a lista [7, 7, 8, 9], chame remove(7) apenas uma vez e explique por que apenas a primeira ocorrencia e removida.

# Remocao por indice
# Monte a lista [1, 2, 3, 4, 5]. Remova o elemento do indice 3 usando pop_at(3) e descreva como as ligacoes mudaram.

# Tamanho e vazio
# Crie uma lista, insira 3 elementos, remova 3 elementos (misturando pop e pop_front) e depois chame size() e is_empty(). Explique os resultados.

# Limpeza geral
# Insira varios valores, chame clear() e explique por que clear() e O(1) mesmo com muitos elementos.

# Erros controlados
# Mostre que pop() em lista vazia dispara IndexError. Explique por que e importante tratar underflow.

# Leitura sequencial
# Percorra a lista manualmente (sem usar imprimir_lista) partindo de _inicio e conte quantos nos existem. Compare com size().




# Desafio 

# Implemente o Bubble Sort usando a sua estrutura Lista encadeada.
# Regras e dicas:

# Nao converta para array; trabalhe percorrendo nos com proximo.

# Voce pode escolher entre:

# Estrategia A (mais simples): fazer as trocas trocando somente os valores dos nos adjacentes.

# Estrategia B (mais avancada): fazer as trocas reencadeando os nos (ajustando os ponteiros proximo).
# Dica: para trocar dois nos adjacentes A e B, voce precisa manter referencia para o no anterior a A. Cuidado com o caso em que A e o primeiro no (_inicio).

# Mantenha uma otimizacao: se em uma passada completa (varrendo a lista) nenhuma troca ocorrer, pare (a lista ja esta ordenada).

# Permita reverse=False/True para ordenar crescente ou decrescente.

# Escreva um pequeno teste (sem acentos) que mostre a lista antes e depois das passadas.