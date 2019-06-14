'''Prática da aula 56'''

'''Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas
mulheres têm menos de 20 anos.'''

homem = ''
idade_homem = 0
quant_homem = 0
mulher = ''
idade_mulher = 0
quant_mulher = 0
idade = 0
media = idade
for itens in range(1, 4+1):
    nome = str(input('Digite o {}º nome: '.format(itens).upper().strip()).upper())
    idade = int(input('Digite a idade da {}ª pessoa. '.format(itens).strip().upper()))
    sexo = str(input('Digite [M ou F] da {}ª pessoa. '.format(itens).upper()).upper())
    media += idade / 4
    if itens == 1 and sexo == 'M':
        homem = nome
        idade_homem = idade
        quant_homem += 1
    if sexo == 'M' and idade >idade_homem:
        homem = nome
        idade_homem = idade
    if sexo == 'F' and idade < 20:
        mulher += nome +', '
        quant_mulher += 1


print('minha media é: {} '.format(media))
print('Homem mais velho tem {}, Seu nome é {}'.format(idade_homem, homem))
print('Temos {} mulheres com mesmo de 20 Anos, e são elas: {} '.format(quant_mulher, mulher))


