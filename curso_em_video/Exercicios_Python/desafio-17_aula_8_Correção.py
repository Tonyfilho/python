'''Fizemos aqui da forma que o prof. ensinou, simplificando
o COD e fazendo de forma fácil'''

import math
co = float(input('Digite o comprimento do Cateto Oposto: '))
ca = float(input('Digite o comprimento do Cateto Adjacente: '))
hip = math.hypot(co, ca)
print(f'O Valor da Hipotenuza É: {hip:.3f}')


