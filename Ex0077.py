nomes_e_notas = [[], [], []];

while True:
    nome_aluno = str(input("Digite o nome do aluno: "));
    nota_aluno_01 = int(input("Digite a primeira nota do aluno: "));
    nota_aluno_02 = int(input("Digite a segunda nota do aluno: "));

    nomes_e_notas[0].append(nome_aluno);
    nomes_e_notas[1].append(nota_aluno_01);
    nomes_e_notas[2].append(nota_aluno_02);
    opcao = str(input("Quer continuar [S|N]: ")).strip().upper();    
    
    if opcao == "S":
        continue
    
    if opcao == "N":
        media = sum(nomes_e_notas[1]) / 2;
        print(f"N. Nome     Média\n" "-"*30);
        for index, posicao in enumerate(nomes_e_notas[0]):
            print(f"{posicao}\n {nome_aluno[0]}\n {media}");
            break