'''Pratica da aula 14 laço while'''
'''
numero = 0
n = int(input('Digite o numero: '))
while n != 0 or n >= 11:
    n = int(input('Digite o numero: '))
    numero = n
print('Numero inválido, tente novamente: ')
for itens in range (1, 10+1):
    tab = n * itens
    print(tab)
    
'''


n = int(input('Digite o numero para taboada: '))
numero = n
while numero != 0 and numero < 11:
    numero += 10
print('numero invalido tente novamento')
for itens in range(1, 10+1):
    tab = n * itens
    print('A Tabuada do numero {} vezes {} é : {}'.format(itens, n, tab))


#    print('taboada')

#    total = n * numero
#    if numero > 10:
#        print('A taboada do {} vezes o numero {} é {} .'.format(n, n * numero, total))
#if numero != 0 and numero >11:












