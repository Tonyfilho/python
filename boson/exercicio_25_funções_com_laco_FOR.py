lista = [1, 2, 3, 4, 5, 6]


# CRIAREMOS UMA FUNÇÃO QUE LEVARÁ ESTES NUMEROS AO QUADRADO
def numero_quadrado(lista):  # VAI receber nossa LISTA como ARGUMENTOS, ou uma array, ou um tupla um dicionario
    retorno = []  # É UMA VARIÁVEL VAZIA, QUE RECEBERÁ O RESULTADO DO NOSSO ARGUMENTO, OU SEJA O QUADRADO DOS NUMEROS
    for i in lista:
        retorno.append(i ** 2)
    return retorno


total_3 = numero_quadrado(lista)  # VARIAVEL RECEBE A FUNÇÃO,  COMO ARGUMENTO A SEGUENCIA DE VALORES A LISTA
for i in total_3:
    print(i)

'''                                  OUTRO EXEMPLO'''


def exemplo(lista):
    retorno = []
    for i in lista:
        retorno.append(i * 10)
    return retorno
total_4 = exemplo(lista)
print(total_4)
for i in total_4:
    print(i)

'''                                   OUTRO EXEMPLO'''
def exemplo_2(lista):
    var_de_retorno = []
    for i in lista:
        var_de_retorno.append(i * 2)
    return var_de_retorno
recebi_var = exemplo_2(lista)
for i in recebi_var:
    print(i)



