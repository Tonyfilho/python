'''Aula sobre DICIONARIOS'''

meu_dicionario_e = {'nome': 'Tony', 'idade': 45}


print(meu_dicionario_e)
#podemos usar alguns paramentros depois do PONTO "."
#aqui imprimiremos o valor do NOME no dicionario,
# ao invez de buscar o indice, pois no dicionario NÃO existe
# indice, temos que buscar por KEY"CHAVES"
#OBS: No DICIONARIO é util para organizar, por dados completos,
# Ex. Nome, End, Tel, Docs e etc.. Além da busca se rápida no
# banco de dados, muito mais rapida e eficiante que a lista.
# OBS.: O Dicionario e o COnjunto são mais eficiente com caso de
# busca de dados.
print(meu_dicionario_e['nome'])
print(meu_dicionario_e['idade'])
'''
foi impresso o valor dentro da chave nome
Tony
45
'''
#podemos contar quantos itens tem no nosso dicionario.
print(len(meu_dicionario_e))
'''
2 "tem dois itens"
'''
print(meu_dicionario_e.values())
'''
dict_values(['Tony', 45])
'''
# O IF foi dentro do DICIONARIO e fez uma busca com
# paramentro VALUE
#podemos dar um busca com o IF.
if 'Tony' in meu_dicionario_e.values():
    print('Tony está aqui na linha 36')
'''
Tony está aqui
'''
#podemos Listar usando o FOR:
for i in meu_dicionario_e.values():
    print(i, 'na linha 42')
'''
Tony "foi impresso os valores da KEY"
45   "foi impresso os valores da KEY"
OBS: Podendo ser impresso fora da ordem
'''
#Podemos mudar os valores e chaves, vamos ver as KEYs "CHAVES"
for i in meu_dicionario_e.keys():
    print(i, 'na linha 50')
'''
nome "foi impresso as KEY"
idade "foi impresso as KEY"
'''
#Podemos modificar os conteúdos, mas
# SEMPRE REFENCIAR AS KEYS "CHAVES" vamos mudar
# os do NOME e da IDADE
meu_dicionario_e ['nome'] = 'JUAN' #Obs. para mudarmos os valores
# da chave tivemos que USAR "[]" ao invés de "{}"
meu_dicionario_e ['idade'] = 12
print(meu_dicionario_e, 'na linha 61')
'''
{'nome': 'JUAN', 'idade': 12}
'''
#Podemos adcionar novos ITENS neste ex. o ENDEREÇO que será criado
# OBS. Para alteração no DICIONARIO tem que usar "[]"

meu_dicionario_e['endereço'] = 'Rua Afonso Castro'
meu_dicionario_e['Tel'] = 918203784
print(meu_dicionario_e, 'na linha 70')

#Podemos da um POP para remover itens

#podemo remover o dicionario dando um .CLEAR















