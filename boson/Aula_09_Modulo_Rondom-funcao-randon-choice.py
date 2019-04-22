
'''Aula_09_Modulo_Rondom, com FUNÇÃO CHOICE, que funciona com STRING,
INTEIROS, FLUTUANTES, BOOLEANOS'''

# RANDOM.CHOICE([lista_itens]) gera ALEATORIAMENTE itens dentro de uma LISTA

import random
lista = ['antonio', 'demora', 'juan', 'outros']
lista2 = [0, 1, 2, 3, 4, 5, 6, 9, 8, 7, 100]

print(random.choice(lista))# a função escolhe dentro da LISTA
# que VOCÊ DETERMINA. ou Seja vc escolhe o que quer ser escolhido.
print('*-*' * 30)
print(random.choice(lista2))
