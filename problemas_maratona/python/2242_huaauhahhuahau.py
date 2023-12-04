# Nesta abordagem ha diversos arquivos de entrada, cada 1 com apenas 1 caso de teste
risada = input()
risada_clean = ''
for index, letra in enumerate(risada):
    if letra in "aeiouAEIOU":
        risada_clean = risada_clean + letra

risada_invertida = risada_clean[::-1]

if (risada_clean == risada_invertida):
    print('S')
else:
    print('N')

