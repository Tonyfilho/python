'''Exercício Python 015: Escreva um programa que pergunte a quantidade de
Km percorridos por um carro alugado e a quantidade de dias pelos quais
ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60
 por dia e R$0,15 por Km rodado.'''

km = float(input('Digite a Kilometragem: '))
dias = int(input('Digite os Dias de Uso: '))
precokm = 60 * km
precodia = 0.15 * dias
total = precokm + precodia

print(f'Você Rodou: {km:.0f} Km', f'\nVocê Usou por {dias:.0f} dias', f'\nTotal a Pagar é: {total:.2f} €')

