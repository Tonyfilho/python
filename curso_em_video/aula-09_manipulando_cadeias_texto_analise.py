'''Prenderemos analizar uma string, nada mais é que sabermos algumas informações , tipo tamanho
com que letra começa, com que letra termina , qual a 1º palavra inteira'''

frase = 'Curso em Video PYTHON'
# LEN mostra o comprimento da variável
print(len(frase), frase.strip())

#COUNT[X] conta um item [X] dentro da variável
print(frase.count('V'))  # vai contar quantos V (MAIUSCULOS) tem dentro da string
# respondendo 1

print(frase.count('o', 0, 14))# Faz a contagem de quantos " o ", dentro deste fatiamento
# respondendo 2 "O" entre o caracter 0 ao 14 temos 2 letras o

print(frase.find('deo' ))# vai encontar quantas palavras com "DEO"
# respondendo na posição nº 11

frase.find('Android')
print(frase.find('Android'))# Vai responder -1, que dizer que não achou nada.

'''Podemos por um objeto dentro do outro objeto, faremos um transformação e uma busca'''
print( 'na posição', frase.lower().find('python'), 'achamos a palavra python')# onde a palavra PYTHON era com caixa alta e fui transformada
# em cx baixa e depois feita a busca.




