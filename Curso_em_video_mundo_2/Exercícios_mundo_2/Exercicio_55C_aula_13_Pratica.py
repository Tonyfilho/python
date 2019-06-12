'''PRATICA DA AULA 55, SEM OLHAR O VIDEO'''
'''                       Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final,
mostre qual foi o maior e o menor peso lidos'''

peso_maior = 0
peso_menor = 0
quant_adulto = 0
quant_crianca = 0
for itens in range(1, 5+1):
    peso = int(input('Digite o peso da {}ª Pessoa: '.format(itens)))
    if itens == 1 and peso > peso_maior > peso_menor:
        peso_maior = peso
        peso_menor = peso
    if peso >= peso_maior and peso >= 45:
        peso_maior = peso
        quant_adulto += 1
    else:
        peso_menor = peso
        quant_crianca += 1

print('O peso maior é: {}, e temos {} com peso de Adultos '.format(peso_maior, quant_adulto))
print('O peso menor é: {}, e temos {} com peso de Crianças '.format(peso_menor, quant_crianca))

