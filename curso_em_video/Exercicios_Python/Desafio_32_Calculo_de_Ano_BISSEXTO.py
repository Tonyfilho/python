'''Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto,
se digitar 0 ele busca  o ano atual e fala se é BISSEXTO '''

import time,  datetime


ano = int(input('Digite um Ano: '))

print('Iremos informar se o Ano {} é ou não bissexto.'.format(ano))
print('PROCESSANDO................Tem um Burro me Olhando......LOL')
time.sleep(3)
if ano == 0:
    ano = datetime.date.today().year #vai pegar o ano ATUAL

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Seu ano é Bissexto: {}' .format(ano))
    print('!#!' * 15)
else:
    print('Seu ano NÃO é Bissesto {}'.format(ano))
    print('!#!' * 15)
