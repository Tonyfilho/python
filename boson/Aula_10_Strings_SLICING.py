'''OPERAÇÃO SLICING que quer dizer FATIAMENTO'''
'''Com fatiamento, ao ínvez de retornamos 1 caracteres podemos retornar 
pedaços ou parte  da variável'''

meu_indice = 'este é o Indice'
minha_lista = meu_indice.split() # transformamos na string em  lista LISTA
print(meu_indice[:])# Onde pegamos toda a variavel quand colocamos os :
print(meu_indice[1:3])#Pegaremos do INDICE
print(f'{minha_lista}')
print('*-*' * 30)
print(minha_lista[-1])  #aqui imprimimos o ultimo item da lista
