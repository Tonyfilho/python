'''Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
preço normal e condição de pagamento: - à vista dinheiro/cheque: 10% de desconto - à vista no cartão: 5% de desconto -
em até 2x no cartão: preço formal - 3x ou mais no cartão: 20% de juros '''

                          # calculo de taxa de juros
from time import  sleep
pagamento = [1, 2, 3, 4]
r_taxa_juros = float(2.00) # Ao mês
a_vista = 1
a_vista_card = 2
card = 3
parcelamento = 4
opcao = 5  # controle para while

print('\033[1;35m'+'programa de calculo de desconto e  pagamento.'.upper() + '\033[m')

                     # 1 WHILE PARA A ESCOLHA DO MENU
while (opcao >=5 or opcao == 0 ):
    print('''\033[1;34mdigite a opção de pagamento do cliente:
    [ 1 ] A Vista com 10% de Desconto
    [ 2 ] A vista no Cartão de Crédito
    [ 3 ] Pagamento no Cartão em 2 x com Preço da Etiqueta
    [ 4 ] Pagamento no Cartão Parcelado acima de 3X com Juros de 2% am.\033[m''')
    opcao += 1
    opcao = int(input('\033[1;35m'+'Digite a opcão de pagamento: \033[m'.upper()).isdigit())
    if opcao >= 5:
        print('\033[1;36m'+'Opcão errada, escolha somente os Numeros do menu\033[m'.upper())
    elif opcao == str(''):
        print('\033[1;36m' + 'Opcão errada, escolha somente os Numeros do menu\033[m'.upper())

print('\033[1;36m' + '*.' * 15 + '\033[m')
print('Estamos processando seu pedido'.upper())
sleep(1)
#                          ESCOLHA DA FORMA DE PAGAMENTO










'''
    print('Estamos processando seu pedido'.upper())
    p_valor_mercadoria = input("Valor presente: ".upper()).strip()
    n_prestacao = input("Quantidade de parcelas: ".upper()).strip()
    t_quantidade_de_prestacao = n_prestacao

'''



'''
                          # Inicio das Condicionais do calculo do JUROS

if (p_valor_mercadoria.isdigit() and r_taxa_juros.is_integer()
    and n_prestacao.isdigit() and t_quantidade_de_prestacao.isdigit()):

    p = float(p_valor_mercadoria)
    r = float(r_taxa_juros) / 100
    n = float(n_prestacao)
    t = float(t_quantidade_de_prestacao)
    a = p * (1 + r / n) ** (t * n)
    valor_parcela = float( a / n )
                              # inicio das impressões

    print("Valor da Compra: {:.2f}".format(p))
    print('Taxa de Juros ao Mês: {:.2f}'.format(r_taxa_juros))
    print('Quantidade de Parcelas Escolhidas: {:.0f}'.format(n))
    print('Total do Parcelamento com Juros: {:.2f}'.format(a))
    print("Valor total a pagar por Mês:{:.2f}".format(valor_parcela))

else:
    print("Um ou mais valores informados são inválidos.")
    
'''