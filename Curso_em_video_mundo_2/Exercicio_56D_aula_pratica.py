'''Prática da aula 56'''

'''Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas
mulheres têm menos de 20 anos.'''

homem = ''
idade_homem = 0
mulher = ''
idade_mulher = 0
quant_mulher = 0
media = 0
quant_total = 0
for itens in range(1, 4+1):
    nome = str(input('Digite o nome da {}ª Pessoa: '.format(itens).strip()))
    idade = int(input('Digite a idade da {}ª Pessoa: '.format(itens)))
    sexo = str(input('Digite [M/F] da {}ª Pessoa: '.format(itens).strip()).upper())
    media += idade / 4
    quant_total += 1

    if itens == 1 and sexo == 'M':
        idade_homem = itens
        homem = nome
    if sexo == 'M' and idade > idade_homem:
        idade_homem = idade
        homem = nome
    if sexo == 'F' and idade < 21:
        mulher += nome + ' '
        idade_mulher = idade
        quant_mulher += 1

print(' A media de anos de {} Pessoas é {}'.format(quant_total, media))
print(' A idade do homem mais velho é: {}, seu nome é: {}'.format(idade_homem, homem))
print(' Temos {} Mulher(es) abaixo de 20 Anos, com idade de: {} , seus nome são {}'.format(quant_mulher, idade_mulher, mulher))
