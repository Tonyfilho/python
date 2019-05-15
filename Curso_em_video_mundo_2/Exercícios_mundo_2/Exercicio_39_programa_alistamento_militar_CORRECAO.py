'''ESTA  É A CORREÇÃO DO EXERCICÍO 39 DE ACORDO COM O VIDEO'''

from datetime import date

atual = date.today().year
nasc = int(input('Digite o Ano de Nascimento: '))
idade = atual - nasc
print('Quem Nasceu em {}, tem {} anos em {}'.format(nasc, idade, atual))
mulher = 1
homem = 2
escolha = (mulher, homem)
print('''Escolha o Sexo que você pertence
[ 1 ] para Mulher
[ 2 ] para Homem''')
if escolha == 1:
    print('Como mulher, você está dispensada de se alistar')
else:

    if idade == 18:
        print('Voce tem que se alistar IMEDITAMENTE!'.capitalize())
    elif idade < 18:
        saldo = 18 - idade
        ano_do_alistamento = saldo + atual
        print('Ainda falta {} anos para o alistamento'.format(saldo).capitalize())
        print('O ano do Alistamento será: {}'.format(ano_do_alistamento).capitalize())

    elif idade > 18:
        saldo = idade - 18
        ano_do_alistamento = atual - saldo
        print('Já passou tantos anos {} do seu alistamento seria {}'.format(saldo, ano_do_alistamento).capitalize())

