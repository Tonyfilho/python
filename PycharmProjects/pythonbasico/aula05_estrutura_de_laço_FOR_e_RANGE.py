'''Esta aula estudamores estrutura de laço FOR E RANGE'''


nomes = ['tony', 'debora', 'juan','fámilia']

#lista_de_numeros = range()
#o RANGE é um FUNÇÃO que vem com PYTHON e cria uma lista de NUMEROS
# Vamos por RANGE(5) e mandarmos imprimir a VARIÁVEL, ele vai fazer, poderia ser
#qualquer coisa além dos numeros, letras, objetos etc.

lista_de_numeros = range(5)
print(lista_de_numeros)
# range(0, 5) AQUI ele imprimiu o OBJETO,
# agora vamos  imprimir usando o FOR.

'''Para da ITEM "numeros" dentro da 
Variável LISTA_DE_NUMERO imprima:'''
for numeros in lista_de_numeros:
    print(numeros)
#olhe que imprimimos:
#0
#1
#2
#3
#4

#Poderiamos falar para começarmos em um nnumero e terminarmos
# em outro, olhe  o exmplo:

lista_de_numeros2 = range(10,15)
for numeros in lista_de_numeros2:
    print(numeros)
#Nós imprimimos de 10 a 15
'''
10
11
12
13
14
'''

# Vamos usar com PASSO agora de 10 em 10 veja abaixo:
lista_de_numeros_com_passo_10 = range(90,200,10)
for numeros in lista_de_numeros_com_passo_10 :
    print(numeros)
#É uma boa maneira de imprimir sÓ numeros PARES ou IMPARES
'''
90
100
110
120
130
140
150
160
170
180
190
'''

# Podemos simlificar o CODIGO e por o RANGE direto
# Veja o exemplo abaixo

for item in range(20,30):
    print(item)
'''
20
21
22
23
24
25
26
27
28
29
'''

# outro exemplo podemo imprimir o INDICE da nossa variavel "NOMES"
nomes_exemplo = ['tony', 'debora', 'juan','fámilia']
for numero in  range(4):
    print(nomes_exemplo [numero])
"""Explicando: o FOR pega a coleção "RANGER" e joga 1  item (1 NUMERO)
dentro da varíavel "NOME" que estava vazia, começando pelo "0 ao 3" Poderia
ser um nome ou um valor, e vai IMPRIMIR o "0, " e volta para FOR novamente imprimi
"depois o 1... "ate acabar """

# OBS: Por convensão USAMOS o I ao invés de ITENS ou NUMEROS
# Olhe o exemplo abaixo:

nomes_exemplo2 = ['tony', 'debora', 'juan','fámilia','Fim_do_exemplo_2']
for i in range(5):
    print(nomes_exemplo2 [i])
#OBS: Caso o RANGE for maior que a LISTA  o programa vai dar erro
# para isto quando temos uma COLEÇÂO fechada não usar o RANGER
# e sim, usar a VARIÁVEL, olhe o exemplo, ao ÍNVEZ de usar um numero:

nomes_exemplo3 = ['tony', 'debora', 'juan','fámilia','Fim_do_exemplo_3']
for i in  nomes_exemplo3:
    print(i)
#OBS: desta forma NÂO precisamos ficar preoculpados na quantidade
#de informações na variável

'''
Desta forma abaixo poderemos usar o RANGE sem dar ERROS
olhe o exemplo
'''
nomes_exemplo4 = ['tony', 'debora', 'juan','fámilia','TERMINAMOS SEM ERROS, NÃO IMPORTA O TAMANHO DA LISTA','Fim_do_exemplo_4']
for i in range(len(nomes_exemplo4)): #ao INVEZ de numero, POR o "LEN" de Tamanho e a variável que
# TEM a LISTA. Olhe acima:
    print(nomes_exemplo4[i]) # Imprima os ITENS da VARIÁVEL "NOMES_EXEMPLO_4
# na NOVA" nova LISTA "i"

''' Com o FOR as possibilidades são enorme vejos abaixo
além de pormos os itens na variável "I",passaremos a adicionar mais 
itens a cada LUPE '''

nomes_exemplo5 = ['tony', 'debora', 'juan','fámilia','ESTAMOS ADD UM "OIEEE p/ cada item','Fim_do_exemplo_5']
for i in range(len(nomes_exemplo5)):
    print(nomes_exemplo5[i])
    nomes_exemplo5.append('Oie')#depois temos que sair da IDENTAÇÂO
# e mandar imprimir a lista completa.
print(nomes_exemplo5)
'''
tony
debora
juan
fámilia
ESTAMOS ADD UM "OIEEE p/ cada item
Fim_do_exemplo_5
['tony', 'debora', 'juan', 'fámilia', 'ESTAMOS ADD UM "OIEEE p/ cada item', 
'Fim_do_exemplo_5', 'Oie', 'Oie', 'Oie', 'Oie', 'Oie', 'Oie']
'''
# ele adcionou o tony,debora, juan, familia etc..e para
# cada vez  que fez, ele adcionou um OIE e no final
# imprimiu uma LISTA











