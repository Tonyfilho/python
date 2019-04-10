'''crie um programa que leia  o nome de  uma pessoa e mostre:'''
'''nome com todas as letras  MAIÚSCULAS e MINUSCULAS, quantidade de letras sem espaços, quantas letras tem
o 1º nome '''

nome = input('Digite seu nome:')
nome_minusculo =  nome.lower()
nome_maiuculo = nome.upper()
nome_sem_espaco = nome.strip()
nome_split = nome.split()

print(f'nome_maiuculo é: {nome_maiuculo}', f'\nnome minusculo é: {nome_minusculo}' f'\nnome sem espaço é: {nome_sem_espaco}')






