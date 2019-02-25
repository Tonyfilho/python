'''
exercicio
faça um programa que pergunte a IDADE O PESO E ALTURA. O sistema tem falar se está  apto
a ser  se alistar no o exercito.
para entrar no exercito é preciso ter:
18 anos
60 kilos
1.70 m

'''

print('Faça seu cadastro para que  o sistema confirme sua inscrição')

nome = input('Digite seu nome completo:')
idade = int(input('Escreva sua Idade:'))  #temos que CONVERTER  para fazer a comparação, Ex. maior menor etc
altura = float(input('Escreva sua Altura: ')) #temos que CONVERTER  para fazer a comparação, Ex. maior menor etc
peso = float(input('Escreva seu Peso: ')) #temos que CONVERTER  para fazer a comparação, Ex. maior menor etc
aprovado = idade, altura, peso




if idade >= 18:
    print('Aprovado em no quesito Idade!')
#  if idade != int:
#      print('entrada de dados ERRADA! Favor repita  o processo:')
elif idade :
    print('Infelizmente você ficou reprovado no quesito Idade !')


if altura >= 1.70:
    print('Aprovado em no quesito altura!')
elif altura:
    print('Infelizmente você ficou reprovado no quesito Altura!')

if peso >= 60:
    print('Aprovado em no quesito Peso!')
elif peso:
    print('Infelizmente você ficou reprovado no quesito Peso !')


print(('Seu Nome:'),nome, ('Sua Idade:'),idade, ('Sua Altura:'),altura, ('Seu Peso:'),peso )


'''Terminamos aqui a primeira parte'''




