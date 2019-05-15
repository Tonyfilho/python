'''Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a
sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''


from datetime import date
ano = int(input('Digite o Ano de Nascimento com 4 Digitos: '))
ano_atual = date.today().year
idade = (ano_atual - ano)
falta_anos = 18 - idade

if idade == 18:
    print('Você Nasceu no Ano: {}. Você esta Apto a se Alistar e tem {} Anos'. format(ano, idade))
elif idade < 18:
    print('Você Nasceu no Ano: {} Falta Apenas {} anos para se Alistar, sua Idade é: {} Anos'.format(ano, falta_anos, idade))
else:
    print('Voce Passou da Idade de Alistamento, terá que Pagar uma Multa, sua Idade é: {}'.format(idade))

