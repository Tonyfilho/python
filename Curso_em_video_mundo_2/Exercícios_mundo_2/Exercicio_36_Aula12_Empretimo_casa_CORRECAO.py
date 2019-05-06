'''Estaremos fazendo a CORREÇÃO de acordo com o CURSO'''
from time import sleep
casa = float(input('Valor da Casa: € '))
salario = float(input('Salário do Comprador: € '))
anos = int(input('Quanto anos de Finaciamento você precisa? '))
pretacao = casa / (anos * 12)
minimo = (salario * 30 ) / 100
print('Para pagar uma casa de €{:.2f}, em {:.0f} anos. ' .format(casa, anos), end='')
print('A Prestação será de € {:.2f}'.format(pretacao))
print('\033[2;35m' + 'PROCESSANDO....' + '\033[m')
sleep(2)
if pretacao <= minimo:
    print('Emprestimo pode ser CONCEDIDO')
else:
    print('Emprestimos NEGADO')

