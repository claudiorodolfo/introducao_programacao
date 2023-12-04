# Usa-se while True com try..except para questoes onde o fim do teste eh determinado por fim de arquivo
# Nesta abordagem ha somente 1 arquivo de entrada com todos os casos de teste
while True:
    try:
        D, Vf, Vg = input().split()

        D = float(D)
        Vf = float(Vf)
        Vg = float(Vg)
    
        S= (D**2+144)**(1/2)
        Tg= S/Vg
        Tf= 12.0/Vf
        if Tg<=Tf:
            print("S")
        else:
            print("N")
    except EOFError:
        break

