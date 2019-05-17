'''                                     Loop FOR como contador'''

'''função RANGE()-Gera uma lista contendo uma PROGRESSÃO ARITMÁTICA.'''
'''O Loop FOR vai fazer uma INTERAÇÃO coma FUNÇÃO RANGE que por sua vez GERA uma LISTA, lembrando que é uma lista
ESPECIAL por ser uma PROGRASSÃO ARITMÉTICA, ou seja  uma seguencia de numeros, e a seguencia de numero poderá ser
ajustada para contagem de numeros de 1 em 1 '''

'''                                           SINTAXE:'''

'''RANGE(INICIO, FIM, SALTO)'''
'''INICIO E SALTO SÃO OPCIONAIS'''
# Senão usar o INíCIO ele assume como ZERO (0)
# Senão usar o SALTO ele assume como UM (1), ou seja sobre de 1 em 1 o valor.

range(11)# VALORES DE 0 A 10
range(5, 11) # VALORES DE 5 A 10, USANDO O PAREMENTRO INICIO
range(2, 51, 2) # VALORES DE 2 A 50 DE 2 EM 2, USANDO PARAMENTRO INICIO E O SALTO

'''Estaremos juntando a função RANGE com o laço  FOR'''
for i in range(11):
    print(i)
for i in range(0, 51, 2):
    print(i)