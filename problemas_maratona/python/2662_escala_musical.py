# Nesta abordagem ha diversos arquivos de entrada, cada 1 com apenas 1 caso de teste
menor = [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0]
nome = ["do", "do#", "re", "re#", "mi", "fa", "fa#", "sol", "sol#", "la", "la#", "si"]
posicoes = [0] * 12
n = int(input()) 

notas = list()
for i in range(n):
    notas.append(int(input()))

for nota in notas:
    posicoes[(int(nota) - 1) % 12] = 1

resposta = -1
for j in range(12):
    encontrado = True

    for i in range(12):
        if posicoes[(j + i) % 12] == 1 and menor[i] == 1:
            encontrado = False
            break
    
    if encontrado:
        resposta = j
        break
  
if resposta != -1:
    print(nome[resposta])
else:
    print("desafinado")

