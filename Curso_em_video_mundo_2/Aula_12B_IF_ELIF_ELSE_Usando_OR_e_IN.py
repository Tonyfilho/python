''' python mundo 2,  '''
''' Aninhamento nada mais  é que por uma extrutura de 
decisao dentro da outra '''
'''Faremos  o mesmo Exemplo aqui da AULA 12, mas de forma simplificada'''

name = str(input('Digite seu nome: ')).strip().capitalize()
if name == 'Antonio' or name == 'Juan' or name == 'Debora':
    print('Nice Name {}'.format(name))
elif name in 'Santa Penha Inacia Leila':# Usamos o IN no LUGAR do == para fazer uma Busca.
    print('This is Family in law name {}'.format(name))
else:
    print('I dont have this name  in my Family')
print('Your name is Commun name {}' .format(name))
