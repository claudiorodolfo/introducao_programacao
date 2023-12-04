# Nesta abordagem ha diversos arquivos de entrada, cada 1 com apenas 1 caso de teste
votos = []
soma_votos = 0
maior_quantidade_votos = 0
n = int(input(""))
#print(n)
if 2 <= n <= 100000:
    for i in range(n):
        votos.append(int(input("")))

    for i in votos:
        soma_votos += i

    if soma_votos > 100000:
        print("Quantidade de votos muito alta")
        False
    else:
        for i in votos:
            if i >= maior_quantidade_votos:
                maior_quantidade_votos = i

    if votos[0] >= maior_quantidade_votos:
        print('S')
    else:
        print('N')

