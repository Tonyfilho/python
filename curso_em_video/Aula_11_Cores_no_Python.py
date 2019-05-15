'''Neste modulo estaremos estudando as corres BÁSICAS
padrão ANSI usadas no PYTHON'''

'''para pormos cores em nosso programas devemos usar: '''
'''\033[0:33:44m '''

'''onde temos  o : TYPE o TEXT e o BACK'''
'''No TYPE temos os numeros :
0 para NONE
1 para BOLD
4 para UNDERLINE
7 para NEGATIVE onde inverte os valores '''

'''no TEXT temos os numeros:
30  BRANCO
31  VERMELHO
32  VERDE
33  AMARELO
34  AZUL
35  ROUXO
36  MAGENTA
37  CINZA
'''
'''NO BACKGROUD
40  BRANCO
41  VERMELHO
42  VERDE
43  AMARELO
44  AZUL
45  ROUXO
46  MAGENTA
47  CINZA
'''

var_teste = 'Teste de Cores'
a = 'AZUL FUNDO VERMELHO'
b = 'VERMELHO FUNDO AZUL'
ola = 'Ola ZOOOOO'
cores = {'limpa': '\033[m',
         'azul': '\033[0;34m'
        ,'amarelo': '\033[0;33m',
         'pretoBranco': '\033[7;30m'}# Criamos uma LISTA de cores
print('\033[0;31m' + var_teste + '\033[m')
print('\033[0;36m' + '*-*' * 10)  # Este  é um SEPARADOR COLORIDO

print('\033[1;31;43m' + var_teste + '\033[m')  # Esta é  forma usando o NEGRITO
print('\033[0;36m' + '*-*' * 10)

print('\033[4;30;45m' + var_teste + '\033[m') # Esta é a forma SUBLINHADO
print('\033[0;36m' + '*-*' * 10)

print('\033[7;30m' + var_teste + '\033[m') # Esta é a forma termos  o fundo BRANCO e a letra PRETA, usando o NEGATIVE
print('\033[0;36m' + '*-*' * 10)

print('Vamos imprimir na cor \033[1;31;44m{0}\033[m , e na cor \033[1;34;41m{1}\033[m'.format(b, a))
print('\033[0;36m' + '*-*' * 10)

print('Vamos imprimir colocando as CORES junto com FORMAT, {}{}{}'.format('\033[4;36m', ola, '\033[m'))
print('\033[0;36m' + '*-*' * 10)
print('Vamos imprimir assim{}{}{}'.format(cores['pretoBranco'], ola, cores['limpa']))
