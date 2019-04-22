'''faça um programa que leia o nome completo de  uma pessoa e, mostrando o 1º e ultimo nome separadamente
ex: Ana Maria dos Santos
primeiro: Ana
ultimo: Santos
'''

nome = str(input('Digite seu nome: ')).strip() .upper()
nome_dividido = nome.split()
print(f'O nome é: {nome_dividido}')
print('O  1º nome é: {}'.format(nome_dividido[0]))
print('O ultimo nome é:{}'.format(nome_dividido[len(nome_dividido)-1])) # tivemos que por o -1, para que ele pegue o
# ultimo nome. Desta forma qualquer tamanho de nome irá funcionar.
