matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]];
pares = [];
for valor01 in range(3):
    for valor02 in range(3):
        try:
            matriz[valor01][valor02] = int(input(f"Digite o valor: "));
                    
            if matriz[valor01][valor02] % 2 == 0:
                pares.append(matriz[valor01][valor02]);
            
        except ValueError:
            print("Digite algo valido!");
            
try:
    for valor01 in range(3):
        for valor02 in range(3):
            print(f"[{matriz[valor01][valor02]}]", end="");
        print();
        
    maior_valor_02_linha = max(matriz[1]);
    soma_valor_03_linha = sum(matriz[2]);
    total_pares = sum(pares);

    print(f"A soma dos numeros pares são: {total_pares}");
    print(f"A soma dos valores da terceira coluna é: {soma_valor_03_linha}");
    print(f"O maior da segunda linha é: {maior_valor_02_linha}");
    
except ValueError:
    print("Erro no codigo!");