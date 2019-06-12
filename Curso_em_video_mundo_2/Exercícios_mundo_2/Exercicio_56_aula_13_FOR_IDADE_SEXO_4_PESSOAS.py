'''Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas
mulheres têm menos de 20 anos.'''



media = 0
maior_idade = 0
media_total = 0
homem = '' # é uma STRING que vai receber os nomes
quant_mulher = 0
print('------{}-----')
for itens in range(1, 4+1):
    nome = input('\033[1;31m'+'Digite o nome da {}ª Pessoa: '.format(itens).upper().strip()+'\033[m')
    idade = int(input('\033[1;32m'+'Digite a idade da {}ª Pessoa: '.format(itens).upper().strip()+'\033[m'))
    sexo = input('\033[1;33m'+'Digite o sexo da {}ª pessoa M ou F: '.format(itens).strip()+'\033[m').upper()
    media += idade / 4
#    print(sexo)
    if itens == 1 and sexo == 'M':
        maior_idade = idade
        homem = nome
    if sexo == 'M' and idade > maior_idade:
        maior_idade = idade
        homem = nome
    if sexo == 'F' and idade < 20:
        quant_mulher += 1





print('A média de Idade é: {} Anos '.format(media))
print('O Nome do Homem mais velho é: {}, e tem {} Anos.'.format(homem, maior_idade))
print('A Quantidade de Mulher(S) abaixo de 20 anos é: {}'.format(quant_mulher))






