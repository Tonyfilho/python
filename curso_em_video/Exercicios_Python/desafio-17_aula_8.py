'''Faça um programa que  leia  o comprimento do
cateto OPOSTO e do cateto ADJACENTE, de um triangulo
retangulo. Calcule e mostre o comprimento da hipotenusa'''


import math

ca = float(input('Digite o valor do Cateto Adjacente: '))
co = float(input('Digite o valor do Cateto Oposto: '))
hip = math.sqrt(ca ** 2 + co ** 2)
valordehip = hip

# Ou Podemos fazer assim:
ca1 = ca
co1 = co
hip1 = (co ** 2 + ca ** 2) ** (1/2)


print(f'Na linha 11 O Valor da Hipotenuza é: {valordehip:.2f}')
print(f'Na linha 16 O Valor da Hipotenuza é: {hip1:.2f}')
