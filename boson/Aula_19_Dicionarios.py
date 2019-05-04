'''DICIONÁRIOS EM PYTHON'''
''' Não são propriamente seguências, mas mais precisamente MAPEAMENTOS'''
'''MAPEAMENTOS também são COLEÇÕES de OBJETOS'''
'''Os Objetos são ARMAZENADOS por CHAVES em vez de POSIÇÕES relativas'''
'''Simplismente mapeiam chaves a valores associados'''
'''São MUTÁVEIS'''

'''DICIONARIOS são uma especiea de extrutura de dados para coletar objetos, a grande diferença entre O DICIONÁRIOS
 e a LISTA é por que  o DICIONARIO guarda por CHAVES e  LISTA  por POSIÇÃO'''

'''Para codificar um DICIONÁRIO usamos {CHAVES} '''
'''Consistem em uma seríe de pares CHAVE:VALOR '''
'''São úteis quando precisamos associar um  conjunto de valores a CHAVE- para  descrever as propriedades de algo.'''
'''EXEMPLO'''

dic = {'produto': 'tigela', 'cor': 'azul', 'preço': 14.00}# temos 1 CHAVE : valor, ex. preço : 14.00

'''Podemos indexar um DICIONARIO para  obter E ALTERAR os VALORES associados as CHAVES'''
'''Porém usamos como "INDEX" uma CHAVE, NÃO uma posição relativa'''
'''EXEMPLO'''
print(dic['produto']) # IMPRIMO O QUE TEM DENTRO DA CHAVE "PRODUTO"
print('\033[2;32m' + '/*/' * 15 +'\033[m')
dic['preço'] += 1 #AUMENTA o valor 1 do no preço
print(dic['preço'])
print('\033[2;32m' + '/*/' * 15 +'\033[m')
'''obs.: PARA ALTERAR OS VALORES DE UM DICIONARIO USAMOS [COCHETES] ao INVÉS  de {CHAVES}'''



