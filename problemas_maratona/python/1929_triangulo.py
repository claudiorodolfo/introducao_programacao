# Nesta abordagem ha diversos arquivos de entrada, cada 1 com apenas 1 caso de teste
entrada = input()
a, b, c, d = entrada.split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)

if abs(b - c) < a < (b + c) or abs(a - c) < b < (a + c) or abs(a - b) < c < (a + b):
    print('S')
elif abs(b - c) < d < (b + c) or abs(d - c) < b < (d + c) or abs(d - b) < c < (d + b):
    print('S')
elif abs(d - c) < a < (d + c) or abs(a - c) < d < (a + c) or abs(a - b) < c < (a + b):
    print('S')
elif abs(b - c) < a < (b + c) or abs(a - c) < b < (a + c) or abs(a - b) < d < (a + b):
    print('S')
else:
    print('N')

