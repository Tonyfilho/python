'''programa que leia uma frase  pelo teclado e mostre:
quantas vezes temos a letra A:

em que  posição ele aparece a primeira vez:

Em que posição ela aparece na ultima vez:


'''

frase = str(input('Digite Uma Frase: ')) .upper().strip()
frase2 = frase.split()

print('A letra "A" aparece quantas vezes {} na Frase '.format(frase.count('A'[0:])))
print('A 1º letra "A" a apreceu na Posição {} da Frase'.format(frase.find('A'[0])))
print('A Ultima letra "A" apareceu na Posição {} da Frase'.format(frase.find('A'[])