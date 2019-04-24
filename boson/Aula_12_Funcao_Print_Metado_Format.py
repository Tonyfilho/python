'''MÉTADO string.FORMAT'''
'''Realiza uma  operação de STRING'''
'''A STRING onde o MÉTADO  é chamado  pode conter TEXTO LITERAL ou CAMPOS DE SUBSTITUIÇÃO delimitados por CHAVES{}'''
'''Estes campos podem conter um INDICE NUMERICO de um argumento posicional'''


minha_variavel = 'PIZZA'
valor = 30
valor2 = 10

print('A {0} custa {1} Euros'.format(minha_variavel, valor))
print('*-*' * 10)
print('Gosto de {0}, mas {1} Euros está caro para um {0} por isto, só pago {2} Euros.'.format(minha_variavel, valor, valor2))
