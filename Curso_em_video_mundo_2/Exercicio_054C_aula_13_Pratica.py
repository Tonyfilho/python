'''Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores.
'''
from datetime import date
maior_idade = 0
menor_idade = 0
nascimento = 0
ano = date.today().year


for itens in range(1, 7+1):
    nascimento = int(input('Digite o ano que vc nasceu a {}, seguido de 4 numero Ex. 19XX: '.format(itens)).strip())
    idade = ano - nascimento
    print(idade)
    if idade >= 21:
        maior_idade += 1
  

    else:
        menor_idade += 1


print('Temos {} pessoas maiores de 21 anos. '.format(maior_idade))
print('temos {} pessoas menores de 21 anos.'.format(menor_idade))

