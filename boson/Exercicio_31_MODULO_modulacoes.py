# ESTA FUNÇÃO EXIBE MENSAGEM DE BOAS- VINDAS:
def mensagens():
    print('\033[0;31m'+'Bem vindo ao nosso exercício 31 de modulos'.upper()+'\033[m')

##FUNÇÃO PARA CALCULO FATORIAL DE UM NUMERO:
def fatorial(numero):
    if numero < 0:
        return 'Digite um numero maior que zero.'
    else:
        if numero == 0 or numero == 1:
            return 1
        else:
            return numero * fatorial(numero - 1)

##FUNÇÃO PARA RETORNAR UMA SERIE DE FIBONACCI ate uma valor X:
def fibonacci(numero_2):
    resultado = [0]
    a = 0
    b = 1
    while b < numero_2:
        resultado.append(b)
        a = b
        b = a + b
    return resultado
