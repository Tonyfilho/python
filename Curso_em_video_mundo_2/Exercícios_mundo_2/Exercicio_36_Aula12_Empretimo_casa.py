'''Exercício 36: Escreva um programa para aprovar a compra de uma casa
. O programa vai perguntar o VALOR do Emprestimo, o Salário do comprador e
a quantidade de Anos que ele vai pagar.
O valor do Emprestimo Não pode passar 30% do Salário, caso aconteça
o Emprestimo é NEGADO.'''
from time import sleep
nome = str(input ('Digite seu Nome Por Favor: ')).strip().capitalize()
emprestimo = float(input('Digite o Valor do Emprestimo Pretendido: '))
salario = float(input('Digite o valor do seu Salário: '))
aprovacao = (salario / 100) * 30
ano = int(input('Digite a Quantidade que anos que Pretende Pagar: '))
prestacao = (emprestimo / ano) / 12
print('\033[2;34m' + '+-+' * 15 + '\033[m')
print('PROCESSANDO.... Tem um BOBO me olhando....LOL')
print('\033[2;34m' + '+-+' * 15 + '\033[m')
sleep(2)
print('A Prestação Base para Calculo será {:.2f}'.format(prestacao))
print('\033[2;34m' + '+-+' * 15 + '\033[m')
if prestacao > aprovacao:
    print('Lamentamos Sr ou Srª. {0}, mas seu emprestimo não foi aprovado'
          '\nO Valor da Prestação deu acima de 30% do seu Salário. '
          '\nSr. {0} tente aumentar o Numero de Prestações' .format(nome))
elif prestacao < aprovacao:
    print('Parabens, Seu emprestimo foi aprovado')
    tempo = ano * 12
    print('A Quantidade de prestação será de : {:.0f} '.format(tempo) + 'Meses.')
    print('A Prestação pretendida será de {:.2f}'.format(prestacao) + '€')

print('\033[2;34m' + '+-+' * 15 + '\033[m')

