'''Aqui nesta aula começaremos a entender o AND  '''

a = 20
b = 50
c = 100

if a < b and 'carro' == 'bicicleta': # aqui fizemos 2 comparações,
    # um com o IF e outra com o AND, onde somente a do IF foi aprovada
    # mas não foi impressa visto que a do AND não foi.
    print(a, 'é menor que :', b)
else:
    print('se o IF estiver certo, mas carro não é = a bicicleta')


'''Vamos fz  outra comparação onde todos são verdadeiro, agora
conseguiremos IMPRIMIR'''

if a < c and 'carro' == 'carro': #olhem que todas são verdadeiras
    print(a, 'É menor que C:',c)
else:
    print('Somente se for FALSO ou se o A for maior que C')


'''Podemos fazer isto usando (PARENTESES) veja como:'''
'''podemos ou não usar os (PARENTESES)'''

if (a<b) and ('João' == 'Maria'): # ou seja ele não imprimiu a linha 26
    print(a, 'É menor que :',b)
else:
    print('João é MACHO e Maria é FEMEA') # E imprimiu a linha  29







