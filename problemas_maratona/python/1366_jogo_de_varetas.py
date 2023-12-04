linhas = int(input()) 

while linhas != 0:
    total = 0
    for i in range(linhas):
        a, b = input().split()

        qtde_varetas = int(b)
        if qtde_varetas % 2 == 1:
            qtde_varetas -= 1;
    
        total += qtde_varetas

    print(total//4)

    linhas = int(input()) 


    


