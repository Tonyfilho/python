'''SEGUENCIAS EM PYTHON'''
'''LISTA É UM DOS TIPO DE SEGUENCIA DO PYTHON'''
'''Uma LISTA é  um tipo de OBJETO que representa uma coleção ordernada.'''
'''As LISTAS podem conter quaisquer  tipo de   OBJETO (STRINGS, NÚMEROS E BOOLEANOS)'''
'''Seus conteúdos pode ser modificado -NÃO SÃO IMITÁVEIS'''
'''Seus Objetos são ACESSADOS a  partir de um INDICES'''
'''LEMBRAM  as extruturas de dados VETOR'''


'''LISTAS'''

'''Uma LISTA pode crescer e diminuir de tamanho.'''
'''São SEGUÊNCIAS MUTÁVEIS'''
'''Uma lista  pode conter outras LISTA como OBJETOS, ou  outro tipo qualquer de seguência'''
'''SUPORTA MÉTADOS que não são suportados  pela STRINGS'''
'''A LISTA pode começar VAZIA e ser preenchida'''

'''criando LISTA, abre e fecha COCHETES e coloque os ITENS caso seja'''
lista = []# Uma Lista vazia
lista_de_numeros = [0, 1, 2, 3, 4, 5]# Lista com números
lista_de_letras = ['a', 'b', 'c', 'd'] # Lista de STRINGS
lista_de_letras_com_sublista = ['a', ['b', 'c', 'd']]
string_transformada_em_lista = 'string'.split()

'''temos os comando LIST que mostra o conteúdo da LISTA'''
list(lista_de_letras)

'''Temos varios METADOS SUPORTADO POR LISTAS'''

concatenado = lista_de_numeros + lista_de_letras # Aqui COCATENAMOS as listas, ou seja JUNTAMOS as.
print('Conteúdo docatenado {}' .format(concatenado))
repeticao = lista * 5 #Aqui repetimos a lista, ou MULTIPLICAMOS ela  por 5 x
print(2 in lista_de_numeros ) # Aqui usa o METÁDO IN p/ buscar dentro da LISTA_DE_NUMERO
# se existe o que buscamos , a resposta é TRUE or FALSE.
print(lista_de_numeros.append(10)) #Aqui o APPEND() acrescenta o itens 10 dentro da LISTA
print(lista_de_numeros)
print(lista_de_numeros.insert(0, 100)) #INSERT() acresenta na POSIÇÂO 0 , o ITEM 100, DESLOCANDO os valores.
print(lista_de_letras.index('d'))#INDEX BUsca de POSIÇÃO por valor
print(lista_de_letras.count('c'))#COUNT Contagem de ocorrênca de "C" na lista
'''Temos o FOR IN'''
for item in  concatenado:#Vai imprimir cada ITEM em uma LINHA

    lista = concatenado
    print('O FOR i  IN lista, ADD o conteúdo da Variável "cocatenado" DENTRO da '
          'Variável LISTA, Conteúdo é: {}'.format(lista))
'''PODEMOS por qualquer nome no lugar do ITEM, normalmente usa -se "I" '''