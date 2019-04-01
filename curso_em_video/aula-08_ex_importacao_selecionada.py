'''Neste Exemplo iremos importar somente um determinado ITEM do
MODULO MATH'''
# Estamos Dizendo.. Do MATH importe somente o SQRT

from math import sqrt
numero = int(input('Digite o Numero: '))
raiz = sqrt(numero) # como estamos importando somente
# 1 modulo da bibliote não preciso escrever math.sqrt,
# somente sqrt(...)

print(f'A Raiz Quadrada do {numero},', f'\nÉ: {raiz:.0f}')
#{raiz:.0f} o :.0F faz com que fique 0 casas depois do PONTO.

