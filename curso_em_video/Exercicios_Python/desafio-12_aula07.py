'''faça um programa que LEIA o preço de uma produto, DÊ 5% de desconto
e mostre  o seu novo  preço já com  o desconto '''

produto = float(input('Digite o valor para produto: '))
desconto = float(input('Digite o valor do Desconto: '))
promocao = produto - (produto * desconto / 100)

print(f'O Desconto é: {promocao}')

