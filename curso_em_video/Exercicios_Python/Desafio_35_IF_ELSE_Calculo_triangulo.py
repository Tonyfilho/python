'''Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem
ou não formar um triângulo.'''

reta_1 = float(input('Digite o tamanho da reta em centrimetros da 1º Reta: '))
reta_2 = float(input('Digite o tamanho da reta em centrimetros da 2º Reta: '))
reta_3 = float(input('Digite o tamanho da reta em centrimetros da 3º Reta: '))
triangulo = 'Triângulo'
print('#+#.' * 15)
if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2:
    print('Estas Medidas  serve para  formar  um {}'.format(triangulo))
else:
    print('Os Valores não formam um {}'.format(triangulo))







