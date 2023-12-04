# Usa-se n != 0 para questoes onde o fim do teste eh determinado por valor 0
# Nesta abordagem ha somente 1 arquivo de entrada com todos os casos de teste
n = int(input())

while n != 0: 
    for i in range(n):
        respostas = input().split(' ')

        opcoes = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}

        marcada = []
        escolha = ''

        for resposta in respostas:
            if int(resposta) <= 127:
                marcada.append(resposta)
                escolha = respostas.index(resposta)

        # verifica se apenas uma resposta foi marcada
        if len(marcada) == 0 or len(marcada) > 1:
            print('*')
        else:
            print(opcoes[escolha])

    n = int(input())

