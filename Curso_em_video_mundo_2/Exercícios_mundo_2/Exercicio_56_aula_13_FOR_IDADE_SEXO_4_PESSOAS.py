'''Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas
mulheres têm menos de 20 anos.'''


nome_1 = {} # Nome_ a Nome_4, são DICs, que irão receber informações de NOME,IDADE e SEXO
nome_2 = {}
nome_3 = {}
nome_4 = {}
media = 0
media_total = media
homem = [] # é uma LISTA que vai receber 4 dicionarios
quant_mulher = 0
for itens in range(1, 4+1):
    nome = input('\033[1;31m'+'Digite o nome da {}ª Pessoa: '.format(itens).upper().strip()+'\033[m')
    idade = int(input('\033[1;32m'+'Digite a idade da {}ª Pessoa: '.format(itens).upper().strip()+'\033[m'))
    sexo = input('\033[1;33m'+'Digite o sexo da {}ª pessoa M ou F: '.format(itens).upper().strip()+'\033[m')
    if itens == 1:
        nome_1 = {'nome': nome, 'idade': idade, 'sexo': sexo}
        media += idade
        if sexo == 'm':
            homem_velho_1 = {'nome': nome, 'idade': idade}
            homem += homem_velho_1

    if itens == 2:
        nome_2 = {'nome': nome, 'idade': idade, 'sexo': sexo}
        media += idade
        if sexo == 'm':
            homem_velho_2 = {'nome': nome, 'idade': idade}
            homem += homem_velho_2

    if itens == 3:
        nome_3 = {'nome': nome, 'idade': idade, 'sexo': sexo}
        media += idade
        if sexo == 'm':
            homem_velho_3 = {'nome': nome, 'idade': idade}
            homem += homem_velho_3

    if itens == 4:
        nome_4 = {'nome': nome, 'idade': idade, 'sexo': sexo}
        media += idade
        if sexo == 'm':
            homem_velho_4 = {'nome': nome, 'idade': idade}
            homem += homem_velho_4

    media_total = media / itens

print(homem)
print('A Média de idade do grupo é {} anos.'.format(media_total))

