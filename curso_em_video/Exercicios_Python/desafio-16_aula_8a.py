'''Crie um programa que leia um numero REAL qualquer
pelo teclado e mostre na tela a sua porção inteira
EX. numero 6.127 tem porção inteira 6. '''

'''Obs: Use a opção MATH'''
import math
n_real = float(input('Digite o Numero Real, seguido por 2 Casas Decimais: '))
n_int = float(math.floor(n_real))

print(f'A porção inteira é: {n_int:.0f}')
# Ou podemos fazer assim como a correção:
print(f'O Valor Digitado é: {n_real}', f'\nO Valor Inteiro é: {math.trunc(n_real)}')
# Ou Podemos fazer sem importar modulos, olhe o Exemplo:
print(f'O Valor usando o outro Exemplo é: {n_real}', f'\nO Valor Inteiro é : {int(n_real)}')
