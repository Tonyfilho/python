'''Pratica da aula 14 laço while'''


n = int(input('Digite o numero para tabuada: '))
numero = n
while numero != 0 and numero < 11:
    numero += 10

    for itens in range(1, 10+1):
        tab = n * itens
        print('A Tabuada do numero {} vezes {} é : {}'.format(itens, n, tab))
if n > 0 and  n < 10+1:
    print('Fim da do programa')
else:
    print('numero invalido tente novamento')













