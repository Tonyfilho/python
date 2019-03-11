'''Falaremos sobre os CONJUNTOS'''

meu_conjunto_e = {'tony', 'debora'}

print(meu_conjunto_e)

#OBS: Objeto do SET "CONJUNTOS" NÃO TEM INDICE ou seja vc
# não pode fazer busca por INDICE:NÂO ESTA ORDENADO EX.print(meu_conjunto_e[0])
#isto daria errado

# print(meu_conjunto_e[0]) TypeError: 'set' object does not support indexing

# para adcionar objeto no meu conjunto tenho que dar um ADD

meu_conjunto_e.add('Juan')
print(meu_conjunto_e)
if 'juan' in meu_conjunto_e:
    print('Juan está aqui no Conjunto' 'Na linha 18')
else:
    print('Aqui n tem Juan''Na linha 20')
'''
Aqui n tem Juan "Olhe que ele entrou no ELSE, pois o JUAN
do conjunto tem "J" MAIÚSCULO "
'''

# Se formos adicionar um OBjeto com o mesmo NOme ele
# Não vai  adcionar, pois no DICIONARIO n pode existir
# itens repeditos. O conjunto vc USARÁ quando vc n quer
# dados REPITIDOS.
# O conjunto tem BUSCA rápida. Se fosse um LISTA e programa
# iria fazer 1 por vez,se tiver 1 BILHÃO de objetos, isto
# ira demorar, ou seja a lista é ordenada e não é ideal
# para se fazer buscar, diferentemente do CONJUNTO e do DICIONARIO.

meu_conjunto_e.add('Juan')
print(meu_conjunto_e, 'Observe que JUAN já existia no meu conjunto na linha 15')
'''
{'debora', 'Juan', 'tony'} olhe , ainda temos 1 JUAN somente
'''
# NO CONJUNTO E DICIONARIO cada OBJETO será transformado em um CODIGO e este
# codigo vira uma TABELA especial chamada "HASH", por isto que a
# busca é instatanea diferentemente da LISTA.

'''
Se o programa ficou lento, é sinal que vc usou algum extrutura errada

'''
