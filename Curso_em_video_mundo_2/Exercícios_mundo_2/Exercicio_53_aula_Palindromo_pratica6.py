'''                                            pratica do exercicio 53 PALINDROMO'''

frase = str(input('Digite a sua palavra ou frase: ').upper().strip())
junto = ''
inverso = ''
for itens in range(1, 2):
    junto = frase[::].replace(' ', '')
    inverso = frase[:: -1].replace(' ', '')
if junto == inverso:
    print('Esta palavra ou frase é um Palindromo!')
else:
    print('Esta palavra ou frase não é um palindromo!')
print(junto, inverso)

