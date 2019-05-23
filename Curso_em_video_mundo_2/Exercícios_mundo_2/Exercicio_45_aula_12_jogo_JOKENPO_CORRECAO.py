'''CORREÇÃO DA AULA 45'''
from random import randint
from time import sleep
print('Vamos começar a JOGAR TURMA.....')
print('O NOME DO JOGO É "PEDRA, PAPEL E TESOURO", TB CONHECIDO COMO JOKENPO')
print('\033[1;35m'+ '[ 0 ] para PEDRA,\n[ 1 ] para PAPEL, \n[ 2 ]para TESOURA''\033[m')
itens = ('Pedra', 'Papel', 'Tesoura')
cpu = randint(0, 2)# ESCOLHA DO COMPUTADOR
print('\033[1;34m'+ 'JO' + '\033[m')
sleep(1)
jogador = int(input('Digite a Sua Jogada: '))# ESCOLHA DO JOGADOR
print('\033[1;30m' + '*-*' * 15 +'\033[m')

print('O JOGADOR escolheu {}'.format(itens[jogador]))
print('\033[1;30m' + '*-*' * 15 +'\033[m')
print('\033[1;33m'+'KEN' + '\033[m')
sleep(1)

print('O COMPUTADOR escolheu {}'.format(itens[cpu]))
print('\033[1;30m' + '*-*' * 15 +'\033[m')
print('\033[1;31m'+'PO.......' +'\033[m')
'''COMPUTADOR JOGOU PEDRA'''
if cpu == 0:
    if jogador == 0:#JOGADOR JOGOU PEDRA
        print('JOGO EMPATADO!!!')
    elif jogador == 1:# JOGADOR JOGOU PAPEL
        print('PAPEL vence Pedra')
        print('JOGADOR WIN!!!')
    elif jogador == 2: #JOGADOR JOGOU TESOURA
        print('PEDRA vence TESOURA')
        print('COMPUTADOR WIN!!!')
    else:
        print('JOGADA INVÁLIDA!!!')

'''COMPUTADOR JOGOU PAPEL'''
if cpu == 1:
    if jogador == 0:  # JOGADOR JOGOU PEDRA
        print('PAPEL vence PEDRA')
        print('COMPUTADOR WIN!!!')
    elif jogador == 1:  # JOGADOR JOGOU PAPEL
        print('JOGO EMPATADO!!!')
    elif jogador == 2:  # JOGADOR JOGOU TESOURA
        print('TESOURA  vence PAPEL')
        print('JOGADOR WIN!!!')
    else:
        print('JOGADA INVÁLIDA!!!')

elif cpu == 2:  #COMPUTADOR JOGOU TESOURA

    if jogador == 0:  # JOGADOR JOGOU PEDRA
        print('PEDRA vence TESOURA')
        print('JOGADOR WIN!!!')
    elif jogador == 1:  # JOGADOR JOGOU PAPEL
        print('TESOURA vence PAPEL')
        print('COMPUTADOR WIN!!!')
    elif jogador == 2:  # JOGADOR JOGOU TESOURA
        print('JOGO EMPATADO!!!')

    else:
        print('Jogada inválida')

