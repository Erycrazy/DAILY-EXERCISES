#MEGA SENA, SORTEIO DE NUMEROS

from random import randint;
from time import sleep;


lista = [];
jogos = [];
quantidade = int(input("Quantos numeros quer sortear: "));

total = 1;
while total <= quantidade:
    contador = 0;
    while True:
        num = randint(1, 60);
        if num not in lista:
            lista.append(num);
            contador += 1;
        if contador >= 6:
            break;
    lista.sort();
    jogos.append(lista[:]);
    lista.clear();
    total += 1;
print(f"Sorteando {quantidade} jogos!");

for indice, listas in enumerate(jogos):
    print(f"Jogo {indice+1}: {listas}");
    sleep(1);
    
print("**BOA SORTE!**");