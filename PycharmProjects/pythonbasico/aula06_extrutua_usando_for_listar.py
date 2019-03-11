
#Passamos a importar nossas variaveis do nosso arquivo MODULO_AULA06,
# com isto n precisamos mais termos todas as variaveis declaradas.
minha_lista_e = ['Tony','Debora', 'Juan']
minha_tupla_e =  ('Tony','Debora','Juan' )
meu_dicionario_e = {'nome': 'Tony', 'idade': 45}
meu_conjunto_e = {'tony', 'debora'}



# a TUPLA de INDICE como a lista, podemos selecionar o que queremos ex:
print(minha_tupla_e[0], 'este é o objeto "0" da minha TUPLA') #pegaremos somente o objeto 0
print(minha_tupla_e[1], 'este é o objeto "1" da minha TUPLA') #pegaremos somente o objeto 1
# podemos dar um FOR para descrever em order a TUPLA
for nome in minha_tupla_e:
    print('Minha lista pelo FOR é: ',nome )
'''
Minha lista pelo FOR é:  Tony
Minha lista pelo FOR é:  Debora
Minha lista pelo FOR é:  Juan
'''
# O FOR pode ser usado em todas as coleções:
# minha_tupla_e.index() veremos que tem poucos METADOS
#  diferente da LISTA que muitos metados.
