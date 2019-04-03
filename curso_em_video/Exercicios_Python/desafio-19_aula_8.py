'''um professor quer sortear um dos seus 4 alunos
para apagar o quadro.Faço um programa que ajude ele.
lendo o nome deles e escrevendo o nome escolhido'''
'''segue o link de consultas do python
https://docs.python.org/3.6/library/index.html
'''
import random
aluno1 = 1, input('Cadastre o Nome para Sorteio: ')
aluno2 = 2, input('Cadastre o Nome para Sorteio: ')
aluno3 = 3, input('Cadastre o Nome para Sorteio: ')
aluno4 = 4, input('Cadastre o Nome para Sorteio: ')
lista = {aluno1, aluno2, aluno3, aluno4}
sorteio = random.randint(1, 4)

print(f'O sorteado foi: {lista}', f'\nO Numero  foi: {sorteio}')
if sorteio == 1:
    print(f'O Sorteado foi :{aluno1} ')
if sorteio == 2:
    print(f'O Sorteado foi : {aluno2}')
if sorteio == 3:
    print(f'O Sorteado foi : {aluno3}')
else:
    print(f'O Sorteado foi : {aluno4}')



