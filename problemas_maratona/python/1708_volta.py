# Nesta abordagem ha diversos arquivos de entrada, cada 1 com apenas 1 caso de teste
a, b = input().split(" ")

a = int(a)
b = int(b)

if 1 <= a <= b and 1 <= b <= 10000:
    contador_volta = 1;
    resta = 0
    while (resta < a):
        resta = contador_volta * (b-a)
        contador_volta += 1

    print(contador_volta)

