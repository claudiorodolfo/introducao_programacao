# Usa-se linha != 0 para questoes onde o fim do teste eh determinado por valores zero
# Nesta abordagem ha somente 1 arquivo de entrada com todos os casos de teste

#dicionario que contem as direcoes
rosa = {
    0:  'N',
    1:  'L',
    2:  'S',
    3:  'O'
}

linha = input()
 
while linha != "0": 
    #recebe a quantidade de comandos
    quantidade_comandos = int(linha)
    comandos = input()

    #define a direcao inicial do soldado
    dir_soldado = 0 #corresponde ao norte

    #itera sobre a lista de comandos
    for com in range(quantidade_comandos):

        #soma para esqueda e subtrai para a direita
        if (comandos[com] == 'E'):
            dir_soldado -= 1
        elif (comandos[com] == 'D'):
            dir_soldado += 1

        #restringe o maximo a 4
        if dir_soldado == 4:
           dir_soldado = 0
        #restringe o minimo a 5
        if dir_soldado == (-1):
           dir_soldado = 3
        
    print(rosa[dir_soldado])

    linha = input()

