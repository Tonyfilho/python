'''estaremos fazendo a correção confirme a video aula, USANDO SOMENTE O IF'''

velocidade = float(input('Digite a sua Velocidade média: '))
print('*-*' * 30)
if velocidade > 80:
    print('Voce foi Multado! ')
    multa = (velocidade - 80) * 7
    print('O valor a pagar da sua Multa: {:.2f}'.format(multa))
print('Dirija com Atenção')
print('*-*' * 30)

