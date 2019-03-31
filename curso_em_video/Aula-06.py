'''faremos um programa que soma 2 valores inteiros de  um VAR'''
n1 = input('Digite aqui o 1º Numero: ')
n2 = input('Digite aqui o 2º Numero: ')

soma = int(n1) + int(n2) # temos que transformar a STRING EM NUMEROS INTEIRO
# usando o INT
print(soma)

'''Esta aula é de TIPOs PRIMITIVOS, segue os 4 mais usados '''
# INT transforma tudo dentro VAR em numero INTEIRO

# FLOAT transforma tudo dentro da VAR em numeros FLUTUANTES ou REAL com ponto EX. 8.40

# BOOL transforma tudo dentro da VAR em valores BOOLEANOS, Ex. Verdadeiro ou Falso,
# sem usar o T de true maisculo e o F de false maiusculo

# STR transforma tudo dentro da VAR em STRINGs, lembrando que temos que USAR "ASPAS"

# Passaremos a USAR um novo PRINT, agora colocando {} EX. PRINT({})
# Colocamos esta MASCARA para que seja subtituida por um METADADO da própria STRING
''' SEGUE O EX
print('colocamos a VAR dentro do PRINT {},' .format(nome da var))
desta forma tudo que que for passar pelo PRINT fica formatado.

'''

print('Olhe na linha 27 o .FORMAT {}' .format(soma))

# é muito mais interessando usar o .FORMAT do que a ("," e o "+") no print
# e é a nova sintax do python 3.0.

'''Vamos usar o atributo TYPE, desta forma veremos  o TIPO da VAR '''

print(type(n2),'Vemos aqui na linha 34, a soma: 69 {}'.format(n2))
'''<class 'str'>'''

n3 = int(input('Digite aqui o numero: '))
n4 = int(input('Digite aqui o numero: '))
var_total = n3 + n4

print('Valor total :{}'.format(var_total))
print(type(var_total))


