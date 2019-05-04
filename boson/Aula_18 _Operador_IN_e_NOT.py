'''OPERADOR IN E NOT'''
'''Os operadores IN e NOT IN  permitem testar se um dado  objeto é membro de uma COLEÇÃO'''
'''Por COLEÇÃO nendemos qualquer  seguência de obletos como  LISTAS, STRINGD, DICIONARIO E TUPLAS'''

'''OBS: uma COLEÇÃO É UMA SEGUENCIA DE  OBJETOS'''

'''SINTAXE DE IN'''
# elemento IN coleção ( ou seja o ELEMENTO X esta  DENTRO  da COLEÇÃO?) É  isto que  o IN faz, é uma BUSCA
# Retorna TRUE  se o elemento for encontrado na coleção,   FALSE  se não for

'''SINTAXE DE NOT IN'''
#elemento NOT IN coleção ( Ou seja o X NÃO EXISTE DENTRO da COLEÇÃO
#Retorna TRUE se  o elemento NÃO for ENCONTRADO na coleção, e FALSE se for
# É A NEGAÇÃO  do elemento IN

'''exemplos:'''
l = ['laranja', 'maçã', 'abacate', 'uva']
if 'abacate' in l:
    print('Sim, a Fruta foi encontrada.')
else:
    print('Não existe Tal Fruta.')
print('\033[4;32m' + '*-*' * 15 + '\033[m')
if 'coco' not in l:
    print('Não temos Coco ainda.')
else:
    print('Já temos Coco')