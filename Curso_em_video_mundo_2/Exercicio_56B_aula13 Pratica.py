'''Prática da aula 56'''

'''Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas
mulheres têm menos de 20 anos.'''

homem_velho = 0
nome_homem = ''
meia = 0
idade = 0
mulher_nova = 0
nome_mulher = ''
media = 0

for itens in range(1, 4+1):
    nome = str(input('------Digite o {}º Nome-----'.format(itens)))
    idade = int(input('------Digite a {}ª Idade------'.format(itens)))
    sexo = str(input('------Escolha o Sexo [M ou F] da {}ª Pessoa: '.format(itens)).upper())
    media += idade / 4
    if itens == 1 and sexo == 'M':
        nome_homem = nome
        homem_velho = idade
    if sexo == 'M' and idade > homem_velho:
        nome_homem = nome
        homem_velho = idade
    if sexo == 'F' and idade < 20:
        mulher_nova += 1
        nome_mulher += 'e' + nome




print('A Media de idade é : {}'.format(media))
print('O homem mais velho é {}, e tem {} Anos'.format(nome_homem, homem_velho))
print('A quantidade de mulher(es) menores de 20 Anos é {}, nome dela(s) {}'.format(mulher_nova, nome_mulher))

