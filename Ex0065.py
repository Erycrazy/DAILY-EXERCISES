#Teste com funções

def verificar_numeros_pares(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

def soma_lista(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado

def minha_lista(lista):
    maior_valor = max(lista)
    return maior_valor

lista = minha_lista([3,2,1,4,3,6,5,4,8,7,1,2,9])

print(lista)