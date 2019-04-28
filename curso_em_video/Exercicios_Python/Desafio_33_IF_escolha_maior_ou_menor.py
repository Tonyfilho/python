'''Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor'''

from time import sleep
n1 = int(input('Digite o 1º Numero: '))
n2 = int(input('Digite o 2º Numero: '))
n3 = int(input('Digite o 3º Numero: '))
print('\033[34m'+'$*$' * 15)
print('\033[35m'+'PROCESSANDO.....Tem BOBO me OLHANDOOOOO.....')
sleep(3)
menor = n1
maior = n1
#Verificando o MENOR
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n1:
    menor = n3
#verificando o MAIOR
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('Os Numeros Digitados foram 1º Numero: {0} 2º Numero: {1} 3º Numero: {2}'.format(n1, n2, n3))
print('$*$' * 15)
print('\033[4;32m'+'O menor numero é: {}'.format(menor))
print('\033[4;33m'+'O maior numero é: {}'.format(maior))
print('-*-' * 15)

