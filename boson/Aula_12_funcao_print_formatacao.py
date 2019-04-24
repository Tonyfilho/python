'''FORMATAÇÃO DE STRINGS'''
'''Os OBJETOS STRINGS possuem uma  operação embutida: %(OPERADOR DE MODULO)   '''
'''Também conhecido como operador de interpolação ou de formatação'''
'''Dados FORMATO % VALORES (em que FORMATO é uma STRING e VALORES geralmente uma VARIÁVEL), as especificações 
de conversão de formato são subtituidas com ZERO ou mais ELEMENTOS DE VALORES'''
'''Similar ao SPRINTF() da liguagem C'''

minha_variavel = 'PIZZA'
numero = 30

'''TIPO DE CONVERSÃO E OS SÍMBOLO DE MODULO'''
'''CARACTERE        TIPO'''
#    d              DECIMAL INTEIRO
#    f              DECIMAL PONTO-FLUTUANTE
#    o              OCTAL
#    x              HEXADECIMAL(x MINUSCULO)
#    X              HEXADECIMAL MAIÚSCULO
#    c              1 CARACTER
#    C              STRING
'''EXEMPLOS'''
print('Vou pedir uma %s '%minha_variavel)#Caracter de formatação para VARIÁVEL
print('/*/' * 10)
print('Ela custa %d Euros ' % numero)#Caracter de formatação no meio da STRING
print('/*/' * 10)
print('A %s custa %d reais' % (minha_variavel, numero))#Caracter de formação mais de uma VALOR ou  VEZ
print('/*/' * 10)
print('')





