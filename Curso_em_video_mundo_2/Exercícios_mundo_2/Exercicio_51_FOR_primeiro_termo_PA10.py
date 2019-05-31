'''Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
 mostre os 10 primeiros termos dessa progressão.'''

print('\033[1;34m' + '==' * 20 + '\033[m')
print(' ' * 10 + '10 termos de um pa'.upper())
print('\033[1;34m' + '==' * 20 + '\033[m')
termo = int(input('Digite o 1º termo : '.upper().strip()))
razao = int(input('digite o numero da razão: '.upper().strip()))
pa = int(input('digite o numero do PA: '.strip().upper()))

for itens in range(1, pa+1 ):
    termo +=  razao
    print('\033[1;34m' + 'O termo de {} é {}'.format(itens, termo).upper() + " -> " + '\033[m')
print('fim'.upper())

print('\n A proporção aritmetrica de : {}, com razão de: {}, tem o termo de: {}'.upper().format(pa, razao, termo

                                                                                              ))