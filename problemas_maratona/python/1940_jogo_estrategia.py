# Nesta abordagem ha diversos arquivos de entrada, cada 1 com apenas 1 caso de teste
quantidade_jogadores, quantidade_rodadas = input().split()
quantidade_jogadores = int(quantidade_jogadores) 
quantidade_rodadas = int(quantidade_rodadas)
quantidade_jogadas = quantidade_jogadores * quantidade_rodadas

jogadas = input().split()


dicionario_jogadores = {}
i = 1
while(i <= quantidade_jogadores):
    dicionario_jogadores[i] = 0
    i += 1
i = 0
j = 1
    
while(i <= quantidade_jogadas - 1):
    pontuacao = int(jogadas[i])
    dicionario_jogadores[j] = dicionario_jogadores[j] + pontuacao
    j = j + 1
    if(j > quantidade_jogadores):
        j = 1
    i = i + 1
vencedor = 0
pontuacao_vencedor = 0
for jogador, pontuacao in dicionario_jogadores.items():
    if(pontuacao >= pontuacao_vencedor):
        pontuacao_vencedor = pontuacao
        vencedor = jogador

print(vencedor)

