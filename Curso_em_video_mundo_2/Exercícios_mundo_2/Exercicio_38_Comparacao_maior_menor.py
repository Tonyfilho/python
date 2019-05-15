'''Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma
mensagem: - O primeiro valor é maior'''

print('\033[1;34mPROGRAMA DE ESCOLHA DO MAIOR NUMERO\033[m')
n1 = int(input('Digite um Numero: '))
n2 = int(input('Digite um Numero: '))
if n1 > n2:
    print('O Nº {} é o maior'.format(n1))
else:
    print('O Nº {} é o maior '.format(n2))