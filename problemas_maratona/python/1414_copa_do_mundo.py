# Usa-se linha != 0 0 para questoes onde o fim do teste eh determinado por valores zero
# Nesta abordagem ha somente 1 arquivo de entrada com todos os casos de teste

linha = input()
 
while linha != "0 0": 
    n_times, n_partidas = linha.split()
    n_times = int(n_times)
    n_partidas = int(n_partidas)

    pontuacao = []
    for line in range(n_times):
        time, pont  = input().split()
        pontuacao.append(int(pont))

    total_pontos = 0
    for ponto in pontuacao:
        total_pontos += ponto

    partidas_x3 = n_partidas * 3

    empates = 0
    if total_pontos < partidas_x3:
        empates = partidas_x3 - total_pontos

    print(empates)

    linha = input()

