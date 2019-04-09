'''Prenderemos analizar uma string, nada mais é que sabermos algumas informações , tipo tamanho
com que letra começa, com que letra termina , qual a 1º palavra inteira'''

frase = 'Curso em Video Phyton'
# LEN mostra o comprimento da variável
len(frase)
#COUNT[X] conta um item [X] dentro da variável
frase.count('V')  # vai contar quantos V (MAIUSCULOS) tem dentro da string
# respondendo 1
frase.count('o', 0, 14)# Faz a contagem de quantos " o ", dentro deste fatiamento
# respondendo 2 "O" entre o caracter 0 ao 14 temos 2 letras o
frase.find('deo')# vai encontar quantas palavras com "DEO"
# respondendo na posição nº 11
print(frase.find('deo'))
frase.find('Android')
print(frase.find('Android'))# Vai responder -1, que dizer que não achou nada.





