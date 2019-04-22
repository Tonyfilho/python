'''Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''


import random

numero = int(input('Digite um Nº de 0 a 5,e tente adivinhar qual o que o computador escolheu: '))
n_escolhido = random.randint(0, 5)
if numero == n_escolhido:
    print('Você acertou o numero cagão: {}'.format(numero))
else:
    print('Tente outra vez: o numero escolhido foi {} '.format(n_escolhido))
