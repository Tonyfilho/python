'''Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final,
mostre qual foi o maior e o menor peso lidos'''


total = []
for itens in range(1, 5+1):
    total.append(input('Digite da {}ª Pessoa: '.format(itens).upper().strip()))
peso_maior = max(total, key=float)
peso_menor = min(total, key=float)

print('O maior preso é: {} KG, e o menor peso é: {} KG'.format(peso_maior, peso_menor))



