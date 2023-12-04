# Usa-se while True com try..except para questoes onde o fim do teste eh determinado por fim de arquivo
# Nesta abordagem ha somente 1 arquivo de entrada com todos os casos de teste

while True:
    try:
        quantidade = int(input())
        ultrapassagens = 0

        # Separando as entradas em listas
        inicio = input().split()
        final = input().split()

        for posicao_inicial in range(quantidade):
            # Recuperando onde o carro X começou e onde terminou na corrida
            carro = inicio[posicao_inicial]
            posicao_final = final.index(carro)

            # Recuperando quais carros estavam na frente do carro X no incio da corrida
            # e quais carros ficaram atrás dele no final
            estava_na_frente = inicio[0:posicao_inicial]
            ficou_atras = final[posicao_final + 1:quantidade]

            # Varre a lista de carros que estava na frente e verifica se o carro X
            # ultrapassou esse carro, se sim soma 1 ultrapassagem
            for frente in estava_na_frente:
                if frente in ficou_atras:
                    ultrapassagens += 1

        print(ultrapassagens)
    except EOFError:
        break

