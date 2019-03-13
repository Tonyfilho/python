'''Vamos criar uma função'''

#Vamos criar uma função que soma 2 numeros
# Para criarmos nossa funcão temos que
# começar escrevendo a palavra "DEF"
# exemplo abaixo de uma função de soma:

def soma(numero1,numero2):
    resposta = numero2 + numero1
    return resposta

#Lembrando como estamos CRIANDO um função, temos
# que definir dentro do (), nada mais são que
# VARIÁVEIS, temos que falar o que vai acontecer
# dentro de soma.
# O que vamos fazer dentro desta função SOMA, ela
# vai somar a variável NUMERO1 e NUMERO2, e jogar
# dentro  da variável "RESPOSTA" e depois temos que dar
# um "RETURN resposta."
# Ou seja ele vai passar pela numero1 e numero2 e
# vai retorna na variável resposta.
# Vamos dar uma exemplo de funcionamento da nossa FUNÇÃO.

#soma(100,155)  precimos CHAMAR e jogar dentro de uma variável
variavel = soma(75,50)
print(variavel)
'''125'''
#A parti de agora posso usar essa função e varias
# parte do  programa nosso programa sem precisar rescrever o cod.
# No PYTHON na criação de FUNÇÔES não preciso ESPECIFICAR  o tipo
# de argumento EX. INT ou FLOAT e nem o tipo de RESPOSTA
# sempre que os argumentos são separado por ","

retorno = soma(12.2,13.7)
print(retorno)
#estamos imprimindo numeros FLOAT, sempre precisar declará ou
# mudar isto na nossa função, o PYTHON faz isto sozinho.
'''25.9'''


