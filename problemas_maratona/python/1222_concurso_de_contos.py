# Usa-se while True com try..except para questoes onde o fim do teste eh determinado por fim de arquivo
# Nesta abordagem ha somente 1 arquivo de entrada com todos os casos de teste
while True:
    try:
        #entrada
        num_palavras_max, num_linhas_max, num_caracteres_max = input().split(" ")
        conto = input()

        #tratando as entradas
        num_palavras_max = int(num_palavras_max)
        num_linhas_max = int(num_linhas_max)
        num_caracteres_max = int(num_caracteres_max)
        conto = conto.split(" ")

        #variaveis
        soma_paginas = soma_linhas = soma_caractere = 0

        #laco para calcular as paginas
        for c, v in enumerate(conto):
            soma_caractere += len(conto[c])

            if soma_caractere >= num_caracteres_max:
                soma_linhas += 1
                soma_caractere = 0
                soma_caractere += len(conto[c])
        
            if soma_linhas >= num_linhas_max:
                soma_paginas += 1

            if ((c + 1) == len(conto)) and (soma_linhas <= num_linhas_max):
                soma_paginas += 1

        print(soma_paginas)
    except EOFError:
        break

