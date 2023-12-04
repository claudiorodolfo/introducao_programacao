# Usa-se linha != "0" para questoes onde o fim do teste eh determinado por valores zero
# Nesta abordagem ha somente 1 arquivo de entrada com todos os casos de teste

linha = input()

while linha != "0": 
    qde = int(linha)
    entrada = input().split()
    executado = [] #Array que armazena os comandos já utilizados por Leandro
    cont = 0

    for e in range(qde):
        if entrada[e] in executado:
            cont = cont + executado.index(entrada[e]) + 1
            executado.insert(0, entrada[e])
        else:
            executado.insert(0, entrada[e])
            if e == 0:
                cont = int(entrada[0])
            else:
                cont = cont + int(entrada[e]) + (len(executado)-1)
    print(cont)

    linha = input()

