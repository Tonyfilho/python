'''estaremos criando um jogo mais conhecido como:'''
'''PEDRA, PAPEL. TESOURA'''

import random
pedra = 0
papel = 1
tesoura = 2
print('Vamos começar a JOGAR TURMA.....')
print('O NOME DO JOGO É "PEDRA, PAPEL E TESOURO", TB CONHECIDO COMO JOQUEPO')
print('\033[1;35m'+ '[ 0 ] para PEDRA,\n[ 1 ] para PAPEL, \n[ 2 ]para TESOURA''\033[m')
numero = int(input('\033[7;30m DIGITE UM NUMERO DE 0 HÁ 2 PARA COMEÇARMOS A JOGAR:\033[m '))
n_escolhido = numero
cpu = random.randint(0, 2)
print('O Numero escolhido foi: {}'.format(n_escolhido))
print('\033[1;30m' + '*-*' * 15 +'\033[m')
print('O Computador escolheu o Numero: {}'.format(cpu))
print('\033[1;31m' + '*-*' * 15 +'\033[m')
if n_escolhido == cpu:
    print('Jogo Empadado, Tente novamente.')
elif cpu == pedra and n_escolhido == tesoura:
    print('Pedra ganha de Tesoura')
    print('COMPUTADOR WIN!')
elif cpu == pedra and n_escolhido == papel:
    print('Papel ganha de Pedra')
    print('JOGADOR WIN!')
elif cpu == tesoura and n_escolhido == papel:
    print('Tesoura ganha do Papel')
    print('COMPUTADOR WIN!')
elif cpu == tesoura and n_escolhido == pedra:
    print('Pedra ganha da Tesoura')
    print('JOGADOR WIN!')
elif cpu == papel and n_escolhido == pedra:
    print('Papel ganha da Pedra')
    print('COMPUTADOR WIN!')
elif cpu == papel and n_escolhido == tesoura:
    print('Tesoura ganha do Papel')
    print('JOGADOR WIN!')
elif n_escolhido >= 3:
    print('Numero Invalido, Comerce novamente.')



