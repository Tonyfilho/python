'''esta é a correção do exercicio 19, igual ao do curso'''

from random import choice
n1 = input('Digite o 1º Aluno: ')
n2 = input('Digite o 2º Aluno: ')
n3 = input('Digite o 3º Aluno: ')
n4 = input('Digite o 1º Aluno: ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print(f'O Aluno Escolhido foi {escolhido}')




