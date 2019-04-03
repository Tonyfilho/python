'''O mesmo professor do desafio anterior quer sortear a orderm
de apresentação de trabalhos dos alunos. Faça um programa
que leia o nome  dos 4 alunos e mostre a order sorteada'''

import random

a1 = input('Digite o Aluno 1: ')
a2 = input('Digite o Aluno 2: ')
a3 = input('Digite o Aluno 3: ')
a4 = input('Digite o Aluno 4: ')
lista = [a3, a2, a1, a4]
escolhido = lista
random.shuffle(escolhido)

print(lista)
print(escolhido)

