'''Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele
é PAR ou ÍMPAR.'''

'''O segredo está ali, no resto. O que sobra.
Ele é o segredo de tudo.

Para saber se um número é par ou ímpar, basta dividir ele por 2.
Se for par, o resto é sempre 0, não sobra nada.
Já se for ímpar, vai sempre ter resto 1.'''

from time import sleep
numero = int(input('Digite uma NUmero: '))
print('PROCESSANDO')
sleep(2)
if 0 == numero % 2:
    print('Seu Numero {} é Par.'.format(numero))
else:
    print('seu numero {} é Impar'.format(numero))

