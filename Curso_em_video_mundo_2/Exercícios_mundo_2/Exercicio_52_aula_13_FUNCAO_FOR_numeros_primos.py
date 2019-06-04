'''Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

'''NUmero PRimo, não pode ser PAR, com exceção do Nº 2, tem que ser IMPAR, e ser DIViDIDO por 1 e somente por ele 
mesmo      '''

'''ESTAREMOS CRIANDO UMA FUNÇÃO COPIADA DO CANAL PYTHON CAFÉ'''
import math
def num_primo(numero):
    raiz = int(math.sqrt(numero))
    for itens in range(2, raiz +1):
        if numero % itens == 0:
            return False
    return True
numero_primo = int(input('Digite um Numero, e falaremos se é Primo: '))
if num_primo(numero_primo):
    print('O numero {} é Primo'.format(numero_primo))
else:
    print(' O numero {} não é Primo' .format(numero_primo))




