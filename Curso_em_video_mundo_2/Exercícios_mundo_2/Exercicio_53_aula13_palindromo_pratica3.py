'''pratica da aula 53 palidromo'''

frase = str(input('Digite a sua frase: ').upper().strip())
lista = frase.split()
#print(lista)
junto = ''.join(lista)
inverso = ''
#print(junto)

for itens in range(len(junto)-1, -1, -1):
    inverso += junto[itens]
print(junto, inverso)

if inverso == junto:
    print('A palavra digitada é um Palindromo')
else:
    print('Isto não é um  palindromo')

