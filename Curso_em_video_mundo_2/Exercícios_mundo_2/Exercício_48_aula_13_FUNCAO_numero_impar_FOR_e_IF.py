'''Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e
 que se encontram no intervalo de 1 até 500.'''


numero = int(input('\033[1;35m'+'Digite um numero, para imprimirmos somente os IMPARES: ' + '\033[m'))
#soma = 0 # Criamos uma VAR SOMA, para receber a soma dos numeros
#contador = 0 # Criamos uma VAR CONTADOR para receber a contagem dos numeros
def numero_impares_somados(*args):
#    global soma
#    global contador
    soma = 0
    contador = 0
    for item in range(1, numero+1, 2):# AQUI FIZEMOS A SEPARAÇÃO SOMENTE DOS NUMEROS IMPARES
        if item % 3 == 0:  #  AQUI perguntamos: SI (ITEM) é "%" DIVISÍVEL por 3, e MULTIPLO de 3
            soma = soma + item
            contador = contador + 1

retorno = numero_impares_somados()
print(retorno)
