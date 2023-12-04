# Usa-se while True com try..except para questoes onde o fim do teste eh determinado por fim de arquivo
# Nesta abordagem ha somente 1 arquivo de entrada com todos os casos de teste
while True:
    try:
        andar = int(input())

        i = 1
        for andar_atual in range(1, andar):
            string_i = str(i)
            #while string_i.find("4") != -1 or string_i.find("13") != -1:
            if string_i.find("4") != -1:
                posicao4 = string_i.find("4")
                i = int(string_i[:posicao4] + "5" +string_i[(posicao4+1):])
                
            string_i = str(i)
            if string_i.find("13") != -1:
                posicao13 = string_i.find("13")
                i = int(string_i[:posicao13+1] + "15" +string_i[(posicao13+3):])

            i += 1

        print(i)
    except EOFError:
        break

