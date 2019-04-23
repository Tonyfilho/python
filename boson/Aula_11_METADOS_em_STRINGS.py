'''METADOS EM STRINGS'''
'''METADOS são como FUNçÔES , mas aplicado a STRINGS'''

metados = 'meus metados'
letras = 'a,b,c,d,e'

print(metados.find('ados')) # encontra a posição de uma substring
print('*/*' * 10)
print(metados.replace('met', 'machuc')) #substitui a ocorrência de uma STRING por outra
print('*/*' * 10)
print(metados.upper())# conversão para caixa alta
print('*/*' * 10)
print(metados.lower())#conversão para caixa baixa
print('*/*' * 10)
print(metados.isalpha())#este é um conteudo ALFABETICA
print('*/*' * 10)
print(metados.isalnum())#é um conteúdo ALFANUMERICO
print('*/*' * 10)
print(metados.strip())# elimina os espaços de uma strind LSTRIP, remove da esquerda RSTRIP da direita
print('*/*' * 10)
print(metados.capitalize())#retona a string com  o 1º caracter em caixa alta
print('*/*' * 10)
print(metados.split())#transforma a string em uma LISTA, e
print(metados.split('a'))#RETORNA lista de itens DETERMINADO  por um caracter ESPECIFICO, removendo o "a"
print('*/*' * 10)
print(letras.split(','))# dizendo pega a STRING e onde vc achar uma VIRGULA vc SEPARA ou split