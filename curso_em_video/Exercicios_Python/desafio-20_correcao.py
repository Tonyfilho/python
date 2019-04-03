'''correção do desafio 20'''

from random import shuffle
n1 = input('Digite aluno 1: ')
n2 = input('Digite aluno 2: ')
n3 = input('Digite aluno 3: ')
n4 = input('Digite aluno 4: ')
lista = [n4, n3, n2, n1]
shuffle(lista)
print(lista)