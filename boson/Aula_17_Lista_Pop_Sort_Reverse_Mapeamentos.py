'''VIDEO 17 LISTA- PARTE02 METADO POP, SORT, REVERSE, MAPEAMENTO'''

'''criando LISTA, abre e fecha COCHETES e coloque os ITENS caso seja'''
lista = []  # Uma Lista vazia
lista_de_numeros = [0, 1, 2, 3, 4, 5]  # Lista com números
lista_bagunca = [3, 4, 5, 8, 1, 6]

lista_bagunca.sort()  # ORDENA A LISTA sem precisar passar ARGUMENTOS, de forma RÁPIDA para ordenar uma lista
print(lista_bagunca)
print('\033[0;34m' + '*+*' * 10 + '\033[m')
lista_bagunca.reverse()  # INVERTEM A ORDEM DA LISTA
print(lista_bagunca)
print('\033[0;34m' + '*+*' * 10 + '\033[m')
lista_de_numeros.remove(5)   # REMOVE o ITEM POR ORDEM DE OCORRÊNCIA
print(lista_de_numeros)
print('\033[0;34m' + '*+*' * 10 + '\033[m')
lista_bagunca.pop(2)  # REMOVE UM ITEM DE UMA POSIÇÃO, NESTE EXEMPLO  da  posição 2
print(lista_bagunca)
print('\033[0;34m' + '*+*' * 10 + '\033[m')
del lista_bagunca[4]   # REMOVE ITEM NA POSIÇÃO de INDICE especifica, nesta order del variavel[posição do item]
print(lista_bagunca)
print('\033[0;34m' + '*+*' * 10 + '\033[m')
del lista_bagunca[1:3]   # REMOVEREMOS UM ITERVALO DE ITENS [0:3] da POSIçÂO 0 há 3
print(lista_bagunca)
print('\033[0;33m' + '*+*' * 10 + '\033[m')
