'''estaremos criando um jogo mais conhecido como:'''
'''PEDRA, PAPEL. TESOURA'''

import random
pedra = int(0)
papel = int(1)
tesoura = int(2)
print('Vamos começar a JOGAR TURMA.....')
print('O NOME DO JOGO É "PEDRA, PAPEL E TESOURO", TB CONHECIDO COMO JOQUEPO')
print('\033[1;35m'+ '[ 0 ] para PEDRA,\n[ 1 ] para PAPEL, \n[ 2 ]para TESOURA''\033[m')
numero = int(input('\033[7;30m DIGITE UM NUMERO DE 0 HÁ 2 PARA COMEÇARMOS A JOGAR:\033[m '))
n_escolhido = numero
print('O Numero escolhido foi: {}'.format(n_escolhido))
print('\033[1;30m' + '*-*' * 15 +'\033[m')
cpu = random.randint(0, 2)
print('O Computador escolheu o Numero: {}'.format(cpu))
print('\033[1;31m' + '*-*' * 15 +'\033[m')
if n_escolhido == cpu:
    print('JOGO EMPATADO, tente novamente!!!')
elif cpu == pedra > tesoura:
    print('COMPUTADOR WIN!!!')
elif cpu == tesoura > papel:
    print('COMPUTADOR WIN!!!')
elif cpu == papel > pedra:
    print('COMPUTADOR WIN!!!')
else:
    print('JOGADOR WIN')