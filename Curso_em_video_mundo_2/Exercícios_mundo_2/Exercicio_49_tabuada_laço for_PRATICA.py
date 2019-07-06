'''Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.'''


tab = int(input('Digite um numero de 1 a 9 para taboada: '))
dig = tab
while tab > 10 or tab == 0:
   print('Digite novamente Um Nº de 1 a 10'.format(dig))
   dig += 1







