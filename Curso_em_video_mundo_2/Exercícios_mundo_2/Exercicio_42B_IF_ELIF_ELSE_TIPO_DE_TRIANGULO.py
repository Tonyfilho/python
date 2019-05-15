'''Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
será formado: - EQUILÁTERO: todos os lados iguais - ISÓSCELES: dois lados iguais, um diferente - ESCALENO: todos os
lados diferentes'''
#                           DESCRIÇÃO DO PROGRAMA
print('\033[1;35m' + 'programa de retas para ver se formão um triângulo.\033[m'.upper())
print('\033[1;34m' + 'o programa também fala que tipo de triangulo temos.\033[m'.upper())
print('\033[1;32m' + '+*' * 15 + '\033[m')
#                              VARIÁVEIS
reta_1 = float(input('Digite o valor da 1º reta: ').upper())
reta_2 = float(input('Digite o valor da 2º reta: ').upper())
reta_3 = float(input('digite o valor da 3ª reta: ').upper())
equilatero = 'Este é um triângulo que tem todos os lados Iguais'.upper()
isosceles = 'Este é um triângulo que tem 2 lados Iguais e 1 diferente'.upper()
escaleno = 'Este é um triângulo que tem  os 3 lados diferentes'.upper()
triangulo = {1: equilatero,  2: isosceles,  3: escaleno}
print('\033[1;33m' + '+*' * 15 + '\033[m')
#                              CONDICIONAIS ANINHADAS:
if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2:
    print('Com estes valores  poderemos criar o triângulo abaixo: '.upper())

    if reta_1 == reta_2 == reta_3:
        print('{}'.format(triangulo[1]))
    elif reta_1 == reta_2 != reta_3 or reta_2 == reta_3 != reta_1 or reta_3 == reta_1 != reta_2:
        print('{}'.format(triangulo[2]))
    elif reta_1 != reta_2 != reta_3:
        print('{}'.format(triangulo[3]))

else:
    print('Com os valores de retas digitados não podemo fazer nenhum dos triângulos '.upper())