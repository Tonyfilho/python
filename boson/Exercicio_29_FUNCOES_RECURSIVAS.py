'''falaremos de RECUSIVIDADE OU RECURSÃO'''

''' RECURSÃO é um métado de siplificação, que consite em dividir um problema em subproblema do mesmo tipo'''
'''Os subproblemas são resolvidos, e seus resultados combinados'''
'''Uma FUNÇÃO RECURSIVA é uma FUNÇÃO   que chama a si PRÓPRIA quando invocada.'''
'''Uma definição de FUNÇÃO RECURSIVA possui um  ou mais CASO-BASE,  para os quais produz um resultado diretamente
sem RECURSÃO, e 1 ou mais  casos RECURSIVOS'''

'''                                   EXEMPLO DE RECURSIVIDADE'''

'''                              Calculo de FATORIAL DE UM NUMERO'''
'''                                 SEGUE A FORMULA DO FATORIAL                   '''
''' FATORIAL(NUM) == 1, se NUM == 0 ou NUM == 1, e 
    FATORIAL(NUM) == NUM * FATORIAL(NUM - 1)
    para NUM > 1 '''

'''                 SEGUE A FUNÇÃO QUE FAZ O FATORIAL DO NUMERO, POR ISTO QUE USAMOS AQUI A RECURSÃO'''

def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1 # NESTE CASO ELE RETORNA O VALOR 1, PARA FUNÇÃO QUE CHAMOU ELE
    else:# SE O NUMERO FOR RECURSIVO ENTRA NO ELSE
        return numero * fatorial(numero - 1)

x = int(input('Digite uma numero para sabermos seu fatorial: '.upper()).strip())


resultado = fatorial(x)
print('O numero {} tem como fatorial {}'.format(x, resultado))

'''                         OUTRO EXEMPLO DE RECUSIVIDADE'''

'''                           usaremos o FIBONACCI RECURSIVO         '''
'''                   A seguência FIBONACCI tb pode ser a parti de uma FUNÇÃO RECURSIVA'''
'''Ela começa com os numeros 0 e 1, e os valores seguintes são somados aos anteriores DELE, como segue:
                                    0, 1, 1, 2, 3, 5, 8, 13, 21, 34.....'''
'''                                 Formula geral para FIBONACCI
    FIBONACCI(NUM) == NUM <= 1 e....
    FIBONACCI(NUM) == FIBONACCI(NUM - 1) + FIBONACCI(NUM - 2)
    para NUM > 1'''

def fibonacci(numero_2):
    if numero_2 <= 1:# podemos por direto assim... IF NUMERO <= 1:
        return numero_2
    else:
        return fibonacci(numero_2 - 1) + fibonacci(numero_2 - 2)

y = int(input(' digite  1 numero para calculo de fibonacci: '.upper().strip()))

resultado2 = fibonacci(y-1)
print('o numero {} tem o fibonacci: {}'.format(y, resultado2).upper())
