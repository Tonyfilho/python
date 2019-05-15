'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
 atleta e mostre sua categoria, de acordo com a idade: - Até 9 anos: MIRIM - Até 14 anos: INFANTIL - Até 19 anos:
 JÚNIOR - Até 25 anos: SÊNIOR - Acima de 25 anos: MASTER'''


print('\033[1;32m' + 'Confederação Nacional de Natação\033[m'.upper())
print('\033[1;30m' + '*-*' * 15 +'\033[m')
print('\033[1;31m' + 'programa de cadastro de nadadores, digite sua idade:\033[m'.upper())
print('\033[1;30m' + '*-*' * 15 +'\033[m')
idade = int(input('idade do atleta: '.upper()))
print('\033[1;30m' + '*-*' * 15 +'\033[m')
if idade <= 9:
    print('Sua  idade é: {} anos, a categoria que você pertence é a mirin.'.format(idade).upper())
elif idade > 9 and idade <= 14:
    print('Sua  idade é: {} anos,  a categoria que você pertence é a infantil.'.format(idade).upper())
elif idade > 14 and idade <= 19:
    print('Sua  idade é: {} anos, a categoria que você pertence é a junior.'.format(idade).upper())
elif idade > 19 and idade <= 25:
    print('Sua  idade é: {} anos, a categoria que você pertence é a senior.' .format(idade).upper())
else:
    print('Sua  idade é: {} anos, a categoria que você pertence é a senior.'.format(idade).upper())




