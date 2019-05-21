'''Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento: - à vista dinheiro/cheque: 10% de desconto -
 à vista no cartão: 5% de desconto - em até 2x no cartão: preço formal - 3x ou mais no cartão: 20% de juros'''

'''APRENDEREMOS ACENTRALIZAR UM TEXTO USANDO O FORMAT o "^" que dizer CENTRALIZADO
O 60 é a quantidade de ESPAÇO, e o = é o que será PREENCHIDO no ESPAÇO'''
print('{:=^60}'.format('\033[1;34m'+' lojas papacu, entrou perdeu maluco!! lol '.upper() + '\033[m'))

preco = float(input('Digite o preço das compras: €  '.upper().strip()))
pag = preco
print('\033[1;34m' + '''escolha a opção de pagamento
[ 1 ] pagamento á vista no dinheiro com 10% de desconto
[ 2 ] pagamento a vista no cartão com 5% de desconto 
[ 3 ] pagamento em 2 x com preço a vista
[ 4 ] pagamento parcelado com 20% de juros '''.upper() + '\033[m' )
opcao = int(input('escolha a opção de pagamento: ').upper())
print('\033[1;33m' + '*0*' * 20 + '\033[m')
print(' Compra foi, {:.2f}€ '.format(preco), end='')
if opcao == 1:
    pag = pag -(pag * 10 / 100)
    print('Valor a vista em dinheiro é {:.2f}'.upper().format(pag))
elif opcao == 2:
    pag = pag - (pag * 5 / 100)
    print('valor a vista no cartão é: {:.2f}'.upper().format(pag))
elif opcao == 3:
    pag = pag / 2
    print('Valor no Cartão será de 2 x de {:.2f} sem juros '.upper().format(pag))
if opcao == 4:
        parcelas = int(input('\n Digite a quantidade de parcelas de 03 há 10x:'.upper().strip()))
        pag = pag / parcelas + (pag * 20 / 100)
        print(' O  parcelamento é {:.2f} x de {:.2f} '.upper().format(parcelas, pag))










