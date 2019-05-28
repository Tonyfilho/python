'''Exercício Python 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de
artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''

from time import  sleep


def contadora(numeros):
    for i in contador:
        print(i)
        sleep(1)
contador = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
retorno = contadora(contador)
print(retorno)

'''

for i in range(1, 11):
    print(i)
    sleep(1)

'''
