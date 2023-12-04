# Nesta abordagem ha diversos arquivos de entrada, cada 1 com apenas 1 caso de teste
import random

# setando os acertos
acertos = 0
# Pegando o numero de jogos
numero_jogos = int(input())
# Iterando a quantidade de jogos para capturar a porta premiada
for jogo in range(int(numero_jogos)):
    # Setando as portas.
    portas = [1, 2, 3]
    # escolhendo a porta premiada
    porta_premiada = portas[int(input()) - 1]
    # primeiramente o jogador sempre escolhe a primeira porta
    porta_escolhida = portas[0]
    # vamos achar a porta que nao e a escolhida e nao e a premiada para abrir
    porta_aberta_com_bode = portas.copy()

    if porta_escolhida is not porta_premiada:
        porta_aberta_com_bode.remove(porta_escolhida)
        porta_aberta_com_bode.remove(porta_premiada)
        porta_aberta_com_bode = porta_aberta_com_bode[0]
    else:
        porta_aberta_com_bode.remove(porta_premiada)
        porta_aberta_com_bode = porta_aberta_com_bode[random.randint(0, 1)]

    # apos isso o usuario sempre muda de porta
    nova_escolha = portas.copy()
    nova_escolha.remove(porta_aberta_com_bode)
    nova_escolha.remove(porta_escolhida)
    nova_escolha = nova_escolha[0]

    if nova_escolha is porta_premiada:
        acertos = acertos + 1

print(acertos)

