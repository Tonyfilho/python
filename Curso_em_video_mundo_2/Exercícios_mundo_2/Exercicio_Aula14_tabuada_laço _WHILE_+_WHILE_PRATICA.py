'''Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.'''

cont = 1
tab = int(input('Digite um numero de 1 a 9 para taboada: '))
dig = tab
while dig != 0 and dig <=10:
#   print('Digite novamente Um Nº de 1 a 10'.format(dig))
   dig += 1
   while cont < 10 + 1:
      print(cont)
      cont += 1
      tabuada = cont *  tab
      print('A tabuada do {} X {} é : {} '.format(cont, tab, tabuada))
print('numero invalido')







