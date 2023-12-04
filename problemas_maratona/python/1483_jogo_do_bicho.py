# Usa-se linha != 0 0 0 para questoes onde o fim do teste eh determinado por valores zero
# Nesta abordagem ha somente 1 arquivo de entrada com todos os casos de teste
"""
Função que recebe um numero em formato de string e retora o mesmo número
com zeros a esquerda se necessário, formando uma string com 4 digitos
Ex: 34 -> 0034
    5263 -> 5263
"""
def completa_numero(numero):
    zeros = ""
    for x in range(0, 4 - len(numero)):
        zeros += "0"
    return zeros + numero

""""
Função que acha o grupo (bicho) ao qual a dezena passada como parametro pertence
EX: 72 -> 19
    44 -> 11
"""
def acha_grupo(dezena):
    if dezena % 4 == 0:
        return dezena // 4
    else:
        return dezena // 4 + 1


linha = input()
 
while linha != "0 0 0":

    valor, num_escolhido, num_sorteado = linha.split()

    num_escolhido = completa_numero(num_escolhido)
    num_sorteado = completa_numero(num_sorteado)

    premio = 0
    valor = float(valor)

    #milhar
    if num_sorteado[-4:] == num_escolhido[-4:]:
        premio = valor * 3000
    #centena
    elif num_sorteado[-3:] == num_escolhido[-3:]:
        premio = valor * 500
    #dezena
    elif num_sorteado[-2:] == num_escolhido[-2:]:
        premio = valor * 50
    #grupo
    elif acha_grupo(int(num_sorteado[-2:])) == acha_grupo(int(num_escolhido[-2:])):
        premio = valor * 16

    print("{:.2f}".format(premio))
    
    linha = input()


