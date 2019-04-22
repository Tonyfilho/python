'''Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
 mostre uma mensagem dizendo que ele foi multado. A multa vai custar €7,00 por cada Km acima do limite.'''


limite = float(80)
multa = float(7)
velocidade_media = float(input('Digite a sua Velocidade Média: '))
velocidade_excedida = (velocidade_media - limite) * multa
print('*-*' * 30)
if velocidade_media <= 80:
    print('Parabens! Dirija com atenção.')
    print('*-*' * 30)
else:
    print('Você utrapassou o Limite de Velocidade: {:.0f}. \nIrá ser multado em {:.0f} € por KM excedido. \nE vai pagar:  {:.0f}€'.format(limite, multa, velocidade_excedida))
    print('*-*' * 30)

