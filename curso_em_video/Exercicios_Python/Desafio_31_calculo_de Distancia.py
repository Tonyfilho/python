'''Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da
passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''

from time import sleep
distancia = float(input('Digite a distância a ser percorrinda na Viagem: '))
print('Voce está para começar uma viagem de {}'.format(distancia))
print('*-*' * 15)
passagem = float(0.50 * distancia)
passagem_longa_dist = float(0.45 * distancia)
print('PROCESSANDO......Tem um Orelha olhando para mim')
sleep(2)
if distancia <= 200:
    print('O Valor da sua Passagem é: {:.2f}'.format(passagem))
else:
    print('O Valor de sua Passagem é: {:.2f}'.format(passagem_longa_dist))
