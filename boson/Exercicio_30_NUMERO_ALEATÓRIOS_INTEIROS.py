'''NESTA AULA ESTAREMOS USANDO  MODULO RANDOM'''
'''Esse modulo possui várias funções para geração de numeros aleatórios, inteiros e de  pondo flutuante,
além de operar sobre seguências, como listas'''

'''OBS: não é indicado para gerar numeros para SEGURANÇA,  é indicado para JOGOS'''

'''numero aleatórios inteiros, temos que importar o MODULO'''

import random

'''Par gerar numeros inteiros temos que usar  sintexes a baixo:'''
# RANDOM.RANDINT(inicio, fim)
'''ONDE  O INICIO É O VALOR QYE INCIA O POOL DE VALORES ALÉATÓRIOS, E O FIM É O VALOR QUE FINALIZA, AMBOS SÃO INCLUIDOS  '''
'''                                             EXEMPLO:'''
retorno = 0
print('-*' * 15)
print('gerando 5 numeros aleatórios entre 1 e 50'.upper())
for itens in range(1, 5+1):
    retorno = random.randint(0, 50)

    print('Os numeros retornados são: {}'.format(retorno))