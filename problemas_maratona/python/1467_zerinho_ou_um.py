# Usa-se while True com try..except para questoes onde o fim do teste eh determinado por fim de arquivo
# Nesta abordagem ha somente 1 arquivo de entrada com todos os casos de teste
while True:
    try:
        escolhas = input().split()
        a = escolhas[0]
        b = escolhas[1]
        c = escolhas[2]

        if a == b == c:
            print ("*")
        elif a == b and a != c:
            print("C")
        elif a == c and a != b:
            print("B")  
        elif b == c and b != a:
            print("A") 
    except (EOFError):
        break
