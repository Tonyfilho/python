'''pratica do exercicio sobre palindromo'''

frase = str(input('Digite a sua frase, ou palavra: ').upper().strip())
for itens in range(1, 2):
    junto = frase[: :].replace(' ', '')
    inverso = frase[: : -1].replace(' ', '')
    if junto == inverso:
        print('A frase ou palavra é um palindromo')
    else:
        print('A frase ou palavra não é um palindromo')

    print(frase, junto, inverso)