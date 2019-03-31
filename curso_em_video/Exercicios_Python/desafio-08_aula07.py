'''escreva um programa que leia em METRO e mostre o valor m
em CENTIMETRO e em MILIMETROS'''

medida = float(input('Digite a medida me Metro: '))
cent = 100 * medida
mili = 1000 * medida

print(f'Sua Medida em Metro é:{medida}' f'\nSua Medida em Centimetro é:{cent}', f'\nSua Medida em Milimetro é:{mili}')
