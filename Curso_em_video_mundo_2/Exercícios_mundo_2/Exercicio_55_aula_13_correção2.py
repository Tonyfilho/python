'''2ª correnção, somente para fixar o cod. na mente, ou seja sem ver'''

maior_peso = 0
menor_peso = 0
for itens in range(1, 5+1):
    peso = float(input('Digite o Peso da {}ª Pessoa: '.format(itens)))
    if itens == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print('O maior Peso é: {}, e o menor Peso é: {}'.format(maior_peso, menor_peso))