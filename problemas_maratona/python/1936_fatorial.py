num = int(input())

def fatorial(n):
    if n <= 1:
        return 1
    else:
        return n * fatorial(n - 1)

def calculamin(min):
    soma_fat = 0 # Registra a soma dos fatoriais
    cont = 1  # Registra a quantidade de numeros fatoriais
    minimo = False
    while not (minimo):
        ant = soma_fat  # Armazena o ultimo estado da soma
        soma_fat = soma_fat + fatorial(min)
        cont = cont + 1
        if soma_fat > num: # verifica se a soma estrapolou o numero desejado
            min = min - 1  # Decrementa para o proximo fatorial
            cont = cont - 1  # Retorna ao estado anterior
            soma_fat = ant # Retorna ao estado anterior
        if soma_fat == num:
            minimo = True
            cont = cont - 1
            print(cont)


def calcula_menor_k():
    emaior = False
    f = 1
    while not (emaior):
        fat = fatorial(f)
        if fat >= num:
            emaior = True
            f = f - 1
            calculamin(f)
        f = f + 1

calcula_menor_k()
