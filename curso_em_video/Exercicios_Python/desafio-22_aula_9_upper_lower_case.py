'''crie um programa que leia  o nome de  uma pessoa e mostre:'''
'''nome com todas as letras  MAIÚSCULAS e MINUSCULAS, quantidade de letras sem espaços, quantas letras tem
o 1º nome '''

nome = str(input('Digite seu nome:')).strip() #colocamos um STRIP na CADEIA de caracteres, com isto removemos os espaços
nome_minusculo =  nome.lower()
nome_maiuculo = nome.upper()
nome_sem_espaco = nome.__len__() - nome.count(' ') #aqui com o - nome.count ele  removeu o espaço ENTRE os NOMES
nome_split = nome.split()

print(f'nome_maiuculo é: {nome_maiuculo} \nnome minusculo é: {nome_minusculo} \nnome sem espaço é: {nome_sem_espaco} '
      f'\nTemos a quantidade de: {nome_split[0]} \n,e temos a quantidade de Letras: {len(nome_split[0])}')






