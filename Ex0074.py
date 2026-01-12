matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]; 

for valor01 in range(3):
    for valor02 in range(3):
        matriz[valor01][valor02] = int(input(f"Digite o valor: ")); 
        
for valor01 in range(3):
    for valor02 in range(3):
        print(f"[{matriz[valor01][valor02]}]", end=""); 
    print(); 