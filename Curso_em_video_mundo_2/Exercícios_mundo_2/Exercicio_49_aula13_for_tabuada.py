'''Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.'''


n_tab = int(input('Digite o numero para Tabuada: '))
for item in range(1, 11):
    tabuada = item * n_tab
    numero = item
    print('A Tabuada do nº {} X {}, é: {}'.format(n_tab, item, tabuada))

