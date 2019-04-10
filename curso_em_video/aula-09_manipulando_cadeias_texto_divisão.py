'''nesta aula veremos a funcionalizade de DIVISÃO,  onde podemores divitir uma cadeia de texto'''

frase = 'Curso em Video Python'
frase2 = frase.split()

'''Estaremos usando o SPLIT mas com a função de OBJETO onde dizemos para ele dividir em 2 nossa variável'''
print(frase.split()) # ele divide a string e transforma em uma LISTA através do seus ESPAÇOS, e TUDO VAI FICAR DENTRO da LISTA.
'''O SPLIT cria uma lista, e cada palavra tem a sua cadeia e caracteres, com a sua divisões individuais'''
#['Curso', 'em', 'Video', 'Python']

'''Etaremos usando o ''.JOIN  desta forma ONDE o que fica entre as ASPAS(' '), irá ser adcionado quando for JUNTAR
   se colocarmos '-' ele apararecerá entre as palavras o - , o JOIN transforma uma LISTA em uma STRING '''
print(' '.join(frase2))# colocamos os espaço entre as ASPAS ' '
#Curso em Video Python
print('**'.join(frase2)) # colocamos ** olhe como ficou:
#Curso**em**Video**Python
print('%%'.join(frase2)) # colocamos %% no lugar do vazio , olhe como ficou:
#Curso%%em%%Video%%Python
'''Iremos mostrar parte da VARIÁVEL FRASE, usando um função di dividir []'''
print(frase[0]) # ele vai mostrar somente quem está n posição "0" zero
#C
print(frase[10]) # mostrou a letra i, que está na  posição 10
#i
print(frase2[2]) #ele vai mostrar o item 2 da LISTA frase2
#Video
print(frase2[2][4]) # ele vai motrar o item 2 da lista frase2 e pegar o item 4 da resposta.
'''estamos dizendo quando colcamos cada um dentro de COCHETE[] , PEGA O ITEM 2 da variável '''
#Video
#o
