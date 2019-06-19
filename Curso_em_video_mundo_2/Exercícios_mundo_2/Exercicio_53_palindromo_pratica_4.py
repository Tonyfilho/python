'''pratica do palindromo'''
frase = str(input('Digite a sua frase: ').strip().strip())
lista = frase.split()
junto = frase[: :].replace(' ', '')
junto2 = ''.join(lista)

inverso = ''
for itens in range(len(junto) -1, -1, -1):
   inverso += junto[itens]
if inverso == junto:
    print('A frase é um palindromo')
else:
    print('A frase não é um palindromo')

print(junto, junto2, inverso)
