# Usa-se linha != "0 0 0 0" para questoes onde o fim do teste eh determinado por valores zero
# Nesta abordagem ha somente 1 arquivo de entrada com todos os casos de teste


linha = input()

#por algum motivo que ainda desconheço o python não entendeu o linha != "0 0 0 0", entrando no laço na última linha dos casos de teste
while linha != "0 0 0 0": 
    #separa a entrada entre espacos
    h1, m1, h2, m2 = linha.split()
    h1 = int(h1)
    m1 = int(m1)
    h2 = int(h2)
    m2 = int(m2)

    #calcula a quantidade de minutos entre dois horarios
    #caso a hora final seja menor que a inicial
    # ou a hora inicial seja igual final e o minuto final seja menor que o inicial
    if (h1 > h2) or (h1 == h2 and m1 > m2):
        h2 += 24

    #converte horas em minutos
    h1 *= 60
    h2 *= 60

    #soma as horas convertidas em minutos com os minutos
    r1 = h1 + m1
    r2 = h2 + m2

    #calcula a quantidade de minutos
    print(r2 - r1)

    linha = input()
    
