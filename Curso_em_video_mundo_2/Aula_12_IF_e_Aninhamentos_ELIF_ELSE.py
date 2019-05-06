''' python mundo 2,  '''
''' Aninhamento nada mais  é que por uma extrutura de 
desisao dentro da outra '''

'''Usaremos IF 
no  o 1º  Bloco '''

'''Usaremos o ELIF
no 2º Bloco  '''

'''Usaremos o ELIF p/
 3º, ou  4º ou 5º BLOCO, '''

'''Usaremos o ELSE 
caso precise do ULTIMO BLOCO'''

'''Temos o OR para usarmos junto com IF ou ELIF'''

nome = str(input('Digite seu nome: ')).strip().capitalize()
if nome == 'Antonio':
    print('Nice name Dear! {}'.format(nome))

elif nome == 'Juan' or nome == 'Debora':
    print('Your name is Beautiful {}'.format(nome))

else:
    print('Seu nome é Comum! {}'.format(nome))
print('Have a nice Day {}!'.format(nome))




