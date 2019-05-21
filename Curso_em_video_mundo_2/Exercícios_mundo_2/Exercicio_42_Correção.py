'''Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
será formado: - EQUILÁTERO: todos os lados iguais - ISÓSCELES: dois lados iguais, um diferente - ESCALENO: todos os
lados diferentes'''


'''ESTA  É A CORRENÇÃO DO EXERCÍCIO O CÓDIGO SERÁ IGUAL AO DA VIDEO'''

r1 = float(input('primeiro segmento: ').upper().strip())
r2 = float(input('segundo segmento: ').upper().strip())
r3 = float(input('terceiro seguimento: ').upper().strip())
# DIGITAREMOS  O CODIGO DE FORMA MAIS LIMPA SEM USAR O "AND" , O PYTHON PERMITE.
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os seguimento acima  podem formar um triângulo ', end='' .upper())
    if r1 == r2 == r3: #ESTAS SÃO AS FORMA SIMPLIFICADAS DO PYTHON
        print('equilátero'.upper())
    elif r1 != r2 !=r3 != r1:  # FORMA SIMPLES SEM O "AND"
        print('escaleno'.upper())
    else:
        print('isósceles'.upper())
else:
    print('os segumento acima  não podem formar um triângulo')