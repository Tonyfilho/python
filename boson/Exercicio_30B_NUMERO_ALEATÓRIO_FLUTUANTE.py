'''Números aleatórios de ponto flutuante'''
import random

'''Para gerar um numeros aleatório de p onto flutuante, usamos a FUNÇÃO RANDOM do MÓDULO conforme  sintaxes A seguir:'''

#RANDOM.RAMDOM()

'''OBS: Essa FUNÇÃO NÃO RECEBE ARGUMENTOS, e gera numeros aleatórios de 0 e 1, podendo ser aumentada por POTÊNCIAÇÃO '''

'''                                                  EXEMPLO'''
print('-*' * 20)
print('Gerando 5 numeros aleatórios de  ponto flutuante, entre 0 e 1' .upper())
for itens in range(1, 6):
    retorno = random.random()
    print(retorno * 10) # MULTIPLICAMOS  POR 10, PARA TERMOS NUMEROS MAIORES DE 0 A 1

'''NUMEROS ALEATÓRIOS DE PONTO FLUTUANTE COM A FUNÇÃO UNIFORM'''

'''Uma outra forma de gerar um numero aleatório de  ponto flutante  é com a função UNIFORM do MÓDULO RANDOM, conforme
a SINTAXES abaixo  '''

#RANDOM.UNIFORM(inicio, fim)

'''Onde o inicio é um valor que fica o POOL de valores aleatórios e o fim, é o valor que finaliza. Ambos incluso na 
faixa'''

print('-*' * 20)
print('Gerando 5 numeros aleatórios de  ponto flutuante,com módulo uniform' .upper())
for itens in range(1, 5+1):
    retorno = random.uniform(0, 1000)
    print(retorno)


'''PODEMOS GERAR NUMEROS ALEATÓRIOS DE DENTRO DE UMA LISTA'''
print('-*' * 20)
print('Gerando 5 numeros aleatórios de  ponto flutuante,com módulo uniform DE UMA LISTA' .upper())
lista = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
for itens in range(1, 5+1):
    retorno = random.choice(lista)
    print(retorno)
retorno_2 = random.sample(lista, 5)  # GERA UMA LISTA DE AMOSTRA ALEATÓRIA DE DENTRO DE OUTRA LISTA(SEGUENCIA + QUANTIDADE)
print(retorno_2)

print('Ordem do random.SAMPLE{}')
print('-*' * 20)
'''podemos novamente embaralhar a nossa lista'''
retorno_3 = random.shuffle(lista)

print('O random.SHUFLLE {}'.format(retorno_3))
print('-*' * 20)