'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços'''

frase = str(input('Digite sua frase: ').strip())
for itens in range(0, 1):
    normal = frase[: :].replace(' ', '')# Damos um replace para tirar o ESPAÇO
    inverso = frase[: : -1].replace(' ', '')
    if normal == inverso:
        print('A Palavra :\033[1;31m {}\033[m escrital Normal e,\033[1;32m {}\033[m escrita Invertida Isto são '
              'palíndromo'.format(normal, inverso))
    else:
        print('A Palavra :\033[1;31m {}\033[m escrital Normal e,\033[1;32m {}\033[m escrita Invertida Isto NÃO são '
              'palíndromo'.format(normal, inverso))








