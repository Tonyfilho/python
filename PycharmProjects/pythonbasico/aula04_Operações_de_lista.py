'''Falaremos  OPERAÇÕES DE LISTAs e Indice'''

frase = 'Ola esta  é uma STRING'
lista_nomes = ['joão','Tony','Debora', 'Juan','joão']

'''aprenderemos como ADD um nome a nossa lista, basta por um "."
veja as opções depois do PONTO EX.:'''

lista_nomes.append('Tonys2') # é a mais usada para ADD itens na lista
print(lista_nomes)
# VEJA o ultimo item,
#OBS.: o APPEND sem add no ultimo lugar da lista
# ['joão', 'Tony', 'Debora', 'Juan', 'joão', 'Tonys2']

lista_nomes.remove('joão') #aqui REMOVEREMOS o nome JOÂO
print(lista_nomes)
#['Tony', 'Debora', 'Juan', 'joão', 'Tonys2']


lista_nomes.insert(0,'Tonys10') #aqui INSERIMOS na POSIÇÂO "0 o nome TONYS10"
print(lista_nomes)

lista_nomes[0] = 'joão' # aqui nós ATRIBUIMOS um nome na POSIÇÂO "0"
print(lista_nomes)
#['joão', 'Tony', 'Debora', 'Juan', 'joão', 'Tonys2']
# ou seja tiramos o Tonys10 e colocamos João

contador_de_nome = lista_nomes.count('joão') #criamos uma VARIÁVEL e
# colocamos o valor lista_nomes dentro desta variável
print(lista_nomes)
print(contador_de_nome)
#['joão', 'Tony', 'Debora', 'Juan', 'joão', 'Tonys2']
# 2 foi a resposta de quantos JOÂOs  temos


'''Da mesma forma que existem ATRIBUTOS para a LISTA, TB existem para o PRINT, 
bastando darmos um PONTO
'''
print(lista_nomes.pop()) #aqui ele tem função de PILHA, pegando
print(lista_nomes)
#sempre o ultimo da lista e REMOVE o item da lista.
#Tonys2
#['joão', 'Tony', 'Debora', 'Juan', 'joão']

'''por fim temos um ATRIBUTO MUITO IMPORTANTE do PRINT onde 
ele media o tamanho da minha lista ou a quantidade  de ITENS 
chamado de LEN '''
print(lista_nomes)
print(len(lista_nomes)) #olhe a resposta
#['joão', 'Tony', 'Debora', 'Juan', 'joão', 'Tonys2']
# 6


lista_nomes.clear() #aqui ele vai imprimir a lista VAZIA
print(lista_nomes)
# []



