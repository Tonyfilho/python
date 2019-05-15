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
equilatero = reta_1 == reta_2 == reta_3
isosceles = reta_1 == reta_2 != reta_3 or reta_2 == reta_3 != reta_1 or reta_3 == reta_1 != reta_2
escaleno = reta_1 != reta_2 != reta_3

print('\033[1;33m' + '+*' * 15 + '\033[m')
#print(equilatero)
#                              CONDICIONAIS ANINHADAS:

if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2:
    print('Os retas com valores {:.0f}, {:.0f}, {:.0f} formam um triângulo'.format(reta_1, reta_2, reta_3).upper())
    if equilatero == True:
        print('Este é triângulo equilátero, tem todos os iquais: lado 1 tem {}, lado 2 {} e lado 3 {}'
          .format(reta_1, reta_2, reta_3).upper())
    elif isosceles == True:
        print('Este é triângulo isosceles, tem 2 lados iguais:  lado 1 tem {}, lado 2 {} e lado 3 {}'.
            format(reta_1, reta_2, reta_3).upper())
    elif escaleno == True:
        print('Este é triângulo escaleno, tem todos os diferentes: lado 1 tem {}, lado 2 {} e lado 3 {}'.
            format(reta_1, reta_2, reta_3).upper())
else:
    print('Os valores digitados não formam retas'.upper())
