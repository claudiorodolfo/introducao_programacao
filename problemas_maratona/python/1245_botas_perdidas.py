# Usa-se while True com try..except para questoes onde o fim do teste eh determinado por fim de arquivo
# Nesta abordagem ha somente 1 arquivo de entrada com todos os casos de teste
while True:
    try:
        quantidade = int(input())

        botas = []
        for x in range(quantidade):
            botas.append(input())

        pares = 0 
        # Enquanto existirem botas na lista de botas
        while (len(botas) > 0):

            # Pegando a primeira bota
            bota = botas[0]
            par_da_bota = ""

            # Se for um bota D o par dela é a E...
            if "D" in bota:
                numero = bota.replace(" D", "")
                par_da_bota = numero + " E"
            else:
                numero = bota.replace(" E", "")
                par_da_bota = numero + " D"

            # Se
            if par_da_bota in botas:
                botas.remove(par_da_bota)
                pares += 1

            botas.remove(bota)

        print(pares)
    except EOFError:
        break

