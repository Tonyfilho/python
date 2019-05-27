'''                            CRIANDO FUNÇÕES EM PYTHON COM ARGUMENTOS'''

'''Como já vimos, definimos uma nova função usandoa INSTRUÇÃO DEF, de acordo com a sintaxes abaixo:'''

# DEF<NOME_FUNÇÃO>(ARGUMENTOS):
#    <INSTRUÇÕES>

'''USAREMOS OU CRIAREMOS UMA FUNÇÃO COM ARGUMENTO ABAIXO:'''
'''Neste exemplo a função SOMARÁ 2 numeros'''

variavel_1 = int(50)
variavel_2 = int(500)

def soma(n1, n2): # AQUI USAREMOS NOME DE VARIÁVEIS COMO ARGUMENTOS
    return n1 + n2 #OBS: Quando usamos o RETURN, dizemos que finalizamos a FUNÇÃO, ou seja retorna quem
    # chamou a função.
'''o RETORNO da função SOMA precisa ser enviado para outra VARIÁVEL OU OUTRA FUNÇÃO'''
total = soma(variavel_1, variavel_2)
print(total)

'''                                INSTRUÇÃO RETURN'''

'''FREGUENTEMENTE USAMOS A  FUNÇÃO RETURN EM UMA FUNÇÃO'''
'''
DEF<NOME_FUNÇÃO>(ARGUMENTOS):
    <INSTRUÇÃO>
    RETURN<VALOR>
'''

'''Ela pode ser declarada em qualquer parte dentro do código da função. Quando execudata, finaliza a chamada de função
 e retorna o resultado de volta a quem fez essa CHAMADA. '''
'''Trata-se de uma instrução opcional, caso não seja utilizada a FUNÇÃO TERMINA, quando finalizar a EXECUÇÃO 
das instruções'''

'''                                EXEMPLO 2      FUNÇÃO QUE SOMA 2 NUMEROS:'''
var_1 = 5
var_2 = 6
def soma_denovo(a,b):
    return a + b
total_2 = soma_denovo(var_1, var_2)
print('A soma de {} e {} é: {}'.upper().format(var_1, var_2, total_2))

'''                                EXEMPLO 3 '''
'''Faremos o python calcular uma seguencia de valores, e RETORNE O RESULTADO, neste caso uma expondeciação'''

'''Vamos criar uma lista, que é uma seguencia'''

lista = [1, 2, 3, 4, 5, 6]

# CRIAREMOS UMA FUNÇÃO QUE LEVARÁ ESTES NUMEROS AO QUADRADO
def numero_quadrado(lista):  # VAI receber nossa LISTA como ARGUMENTOS, ou uma array, ou um tupla um dicionario
    retorno = []  # É UMA VARIÁVEL VAZIA, QUE RECEBERÁ O RESULTADO DO NOSSO ARGUMENTO, OU SEJA O QUADRADO DOS NUMEROS
    for i in lista:
        retorno.append(i ** 2)
    return retorno


total_3 = numero_quadrado(lista) # VARIAVEL RECEBE A FUNÇÃO,  COMO ARGUMENTO A SEGUENCIA DE VALORES A LISTA
for x in total_3:
    print(x)






