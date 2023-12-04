# Nesta abordagem ha diversos arquivos de entrada, cada 1 com apenas 1 caso de teste
c1, c2, c3 = input().split()
c1 = int(c1)
c2 = int(c2)
c3 = int(c3)
if (c1-c2 == 0) or (c1-c3 == 0) or (c2-c3 == 0):
    print('S')
else:
    if(c1+c2-c3 == 0) or (c1+c3-c2 == 0) or (c2+c2-c1 == 0):
        print('S')
    elif(c1-c2-c3 == 0) or (c2-c1-c3 == 0) or (c3-c1-c2 == 0):
        print('S')
    else:
        print('N')

