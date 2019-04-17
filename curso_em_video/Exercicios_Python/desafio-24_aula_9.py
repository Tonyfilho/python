'''desafio 24 crie um programa que  leia um nome de  uma cidade e diga se ela começa ou não com o nome SANTO '''

nome_da_cidade = str(input('Digite o nome da Cidade que nasceu: ')).strip()

print(nome_da_cidade[:5].upper() == 'SANTO')

