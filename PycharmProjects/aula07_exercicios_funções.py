'''Criaremos uma função em que respoderá sempre  o maior ITEM
dentro dela e tb criaremos outra que responderá o menor'''

def maior (i):
    maior_item = i[0]
    for numero in i:
        if numero > maior_item:
            maior_item = numero
        return maior_item

print(maior([5,10,100,1,-50,30,887,999,5]))

def menor (colecao):
    menor_item = colecao[0]
    for item in colecao:
        if item < menor_item:
            menor_item = item
        return menor_item
print(menor([-100,-500,1,50,-1000,0]))



