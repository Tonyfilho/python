'''
Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
import datetime
maior = 0
menor = 0
data = datetime.date.today().year

for itens in range(1, 7+1):
    idade = int(input('Cadastre o ano de Nascimento: '))
    if data - idade >= 18:
#        print('Vc é de maior')
        maior += 1
    else:
#        print('Vc é de menor')
        menor += 1
print(' temos' + ' \033[1;31m{0}\033[m' +  'nascimentos de menores, e' + ' \033[1;32m{1}\033[m' +  'nascimento de maiores'.format(menor, maior).upper())


