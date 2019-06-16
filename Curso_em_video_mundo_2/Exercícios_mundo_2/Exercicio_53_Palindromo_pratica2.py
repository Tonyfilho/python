'''pratica do PALINDROMO USANDO O REPLACE'''
frase = str(input('Digite a frase: ').upper().strip())
lista = frase.strip()
inverso = ''
normal = frase[: :].replace(' ', '')

for itens in range(len(lista)-1 -1 -1 ):
    inverso += normal[itens]
if inverso == normal:
    print('A palavra {} é um Palindromo, pois é iqual ao seu inverso da palavra: {}'.format(normal, inverso))
else:
    print('Esta frase ou palavra não é um Palindromo')