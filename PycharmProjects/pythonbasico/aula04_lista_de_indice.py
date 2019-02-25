'''Falaremos sobre lista e Indice'''

frase = 'Ola esta é uma String'

lista_nome = ['joão', 'Tony','Debora', 'Juan', 'Isto é uma lista, com varios nomes ou endereço, ou comandos']

print(frase) #aqui ele vai imprimir nossa STRING
print(lista_nome) #aqui ele vai imprimir nossa LISTA ate co os COCHETES E VIRGULAS
#Transformando a lista em um STRING e sendo impressa.

print(frase[0]) # aqui ele vai imprimir somente a letra "O"
print(frase[12]) # aqui ele vai imprimir o ITEM 12 a letra "M"
print(frase[-1]) # aqui ele vai imprimir o ULTIMO ITEM a letra "G"
print(frase[0:5])# Aqui imprimimos do ITEM "0" ao "5" "Ola_e"
print(frase[3:15])# Aqui imprimimos do ITEM "3" ao "15" "_esta é uma"
print(frase[3:15:2])# Aqui imprimimos do ITEM "3" ao "15" com Steep ou Passo "2" e ficou "_saéua"
# ou seja ele vai pular de 2 em 2 a impressão. o padrão é 1.
print(lista_nome [0:2]) # aqui da mesma forma vamos imprimir do "0" ao
#ao "1" sendo que contamos 2 ['joão', 'Tony']
print(lista_nome [0:5:2]) # Aqui imprimimos do ITEM "3" ao "15" com Steep ou Passo "2" e ficou "_saéua"
#['joão', 'Debora', 'Isto é uma lista, com varios nomes ou endereço, ou comandos']
print(lista_nome[-1])#onde passamos valores NEGATIVOS, desta forma ele imprime o ULTIMO
print(lista_nome[-1:-4:-2])#aqui colocamos NEGATIVO com o PASSO negativo tb
# como podemo ver ele inverte a lista ['Isto é uma lista, com varios nomes ou endereço, ou comandos', 'Debora']
# OBS.: normalmente usaremos 1 INDICE SÓ, ou a lista toda
print(lista_nome[::-1])# aqui ele inverte toda a lista quando usao o PASSO negativo veja abaixo:

