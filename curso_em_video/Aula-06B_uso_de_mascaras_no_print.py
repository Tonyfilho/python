'''Aprenderemos usar as MASCARAS no print, com isto ficará mais fácil'''

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n_total = n2 / n1
# faziamos assim, quando queriamos dar uma print nas variáveis:
print('A Divisão entre: ', n1, ' e ', n2, ' É :,{}'.format(n_total))

'''Da nova forma podemo fazer assim, usando mas MASCARAS'''
print('A Divisão entre {} e {} da linha 12 vale {}'.format(n1, n2, n_total))
# a divisão da 1ª COISA, entre a 2ª COISA é a 3ª COISA.
