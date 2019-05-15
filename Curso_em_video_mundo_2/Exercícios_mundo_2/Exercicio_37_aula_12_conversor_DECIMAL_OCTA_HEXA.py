'''Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''

from time import sleep
                                        #Aqui começa nossas variáveis
numero_inteiro = int(input('Digite um Numero para conversão: '))
numero_hexa = hex(numero_inteiro)
numero_octa = oct(numero_inteiro)
numero_bina = bin(numero_inteiro)
lista = {numero_hexa: 0, numero_octa:1, numero_bina:2}

                                        # aqui começa os cochetes de opções
print('''Segue as opções de CONVERSÃO
\n\033[1;31m[ 0 ] O para que o Nº:{0} Inteiro, seja converdido em Hexadecimal \033[m
\n\033[1;32m[ 1 ] O para que o Nº:{0} Inteiro, seja converdido em Octal\033[m
\n\033[1;34m[ 2 ] O para que o Nº:{0} Inteiro, seja converdido em Binário\033[m'''.format(numero_inteiro))

                                        # Aqui começa a Opção de Escolha, com uso de condições ANINHADAS
print('\033[1;36m *-*' * 15 + '\033[m')
print('\033[1;37mESCOLHA A OPÇÃO DE CONVERSÃO\033[m')
escolha = int(input())
print('PROCESSANDO......TEM BOBO ME OLHANDO.....')
sleep(1)
print('\033[1;36m *-*' * 15 + '\033[m')
print('\033[1;35mA opção Escolhida foi: {}\033[m'.format(escolha))
print('\033[1;36m *-*' * 15 + '\033[m')
                                        # Aqui começa as nossas Extruturas de Decisões

if lista[numero_hexa] == escolha:
    print('Seu Numero Hexadecimal é: {}'.format(numero_hexa[2:]))#  COLOCAMOS [2:] PARA FATIAR A RESPOSTA esconder o 2s 1º NUmeros que são codigos do  PYTHON
elif lista[numero_octa] == escolha:
    print('Seu Numero Octal é: {}'.format(numero_octa[2:]))#  COLOCAMOS [2:] PARA FATIAR A RESPOSTA esconder o 2s 1º NUmeros que são codigos do  PYTHON
elif lista[numero_bina] == escolha:
    print('Seu Numero Octal é: {}'.format(numero_bina[2:]))
#  O [2:]FATIA A STRING, ELIMINADO OS 2º NUMEROS DE CONTROLE DO PYTHON
else:
    print('OPÇÃO ERRADA TENTE NOVAMENTE')




