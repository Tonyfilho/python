'''Neste Exemplo importaremos a biblioteca RANDOM'''

import random
numero = random.random
print(f'\n O Numero É: {numero}')

numero2 = random.randint(1, 20)# com random.randint ele cria numero aleatorios de 1 a 20
print(f'O Numero É: {numero2}')