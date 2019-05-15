'''ANINHAMENTO DE EM DICIONÁRIOS'''
#  USA-SE {CHAVES}, somente para CRIAR UM DICIONÁRIO, USA -SE [COCHETES] para fazer OPERAÇÕES no DICIONÁRIO

'''Podemos criar uma estrutura de DICIONÁRIO por meio  ANINHAMENTO para que ahja suporte à multiplas partes,
usando por exemplo LISTAS  ou DICIONÁRIOS como ITENS.'''

'''EXEMPLO DE EXTRUTURA DE DICIONÁRIO ANINHADA'''


'''Temos um DICIONÁRIO, que seu valor é OUTRO DICIONÁRIO, que temos 1 TUPLA, podemos ter uma LISTA, ou qualquer
OUTRO tipo de dados '''

'''neste EXEMPLO acima , temo a chave NOME: e o valor { é outro DICIONÁRIO com CHAVE PRIMEIRO_NOME VALOR Antonio
 CHAVE SOBRE_NOME VALOR filho'''

'''Depois na continuação temos uma CHAVE CONHECIMENTO com valor uma TUPLA, com vário ITÉNS dentro, desta forma
NÃO PRECISAMOS ficar criando varias CHAVES EX. conhecimento_1, conhecimento_2  etc. para isto que server o ANINHAMENTO
DE DICIONÁRIO   '''

dic = {'nome':{'primeiro_nome': 'Antonio', 'sobre_nome': 'filho'}, 'conhecimentos':['Python', 'CSS', 'HTML'],
       'idade':46}
print('\033[1;35m' + '*-' * 25 + '\033[m')
'''OPERAÇÕES DE DICIONARIOS'''
print(dic['nome']) #  ELE  VAI IMPRIMIR A CHAVE NOME, ou seja o nome completo
'''OBS: que usamos [CHAVES] para SELECIONARMOS os ITENS  do DICIONÁRIO'''
print('\033[1;35m' + '*-' * 15 + '\033[m')

print(dic['nome']['primeiro_nome'])# usamos 2 [CHAVES] ou  INDÍCE DUPLO ALINHADAS, onde imprimiremos
# O 1º VALOR DA CHAVE NOME
print('\033[1;35m' + '*-' * 15 + '\033[m')

print(dic['conhecimentos'])# IMPRIME a LISTA "conhecimento" completa
print('\033[1;35m' + '*-' * 15 + '\033[m')

print(dic['conhecimentos'][-1])# IMPRIME  da LISTA "conhecimento" o ÚLTIMO item, OUTRO EX. de INDÍCE DUPLO
print('\033[1;35m' + '*-' * 15 + '\033[m')

dic['conhecimentos'].append('IPV6') #ADICIONAMOS ou INSERE o VALOR "ipv6" na LISTA conhecimento, DENTRO do DIC
print(dic)
print('\033[1;35m' + '*-' * 15 + '\033[m')