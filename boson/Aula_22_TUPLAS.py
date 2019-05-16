'''TUPLAS'''
'''A TUPLA  é uma espécie de LISTA que não pode ser ALTERADA, ou seja é IMUTÁVEL, é um seguência com uma  lista
, mas não pode ser alterada, como uma STRING'''
'''São codificadas entre (PARÊNTESES) e  suportam tipos diferentes de dados, aninhamentos e operações normais de 
seguências.'''
'''EXEMPLOS DE TUPLAS:'''
tupla = ('abacaxi', 'abacate', 'carambola', 'pitanga')
tupla_2 =('palavra', 2, ['a', 'b', 'c'])# Um TUPLA com 3 itens, sendo 1 STRING, 1 INTEIRO, e uma LISTA ANINHANDO

print(tupla)
print(tupla_2)
'''                    OPERAÇÕES COM TUPLAS'''
print(len(tupla_2)) # MOSTRA O COMPRIMENTO DA TUPLA

print(tupla_2.index('palavra'))# MOSTRA A POSIÇÃO DO ITEM "PALAVRA"

print(tupla_2.count('abacaxi')) # CONTA QUANTAS PALAVRAS ABACAXI EXITEM NA TUPLA

print(tupla[2])#  MOSTRA O 3º ELEMENTO DENTRO DA TUPLA

print(tupla_2[2][1]) # BUSCA O ELEMENTO NA POSIÇÃO 3[lista] e BUSCA O ITEM 2 DA LISTA
