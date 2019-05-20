'''Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
preço normal e condição de pagamento: - à vista dinheiro/cheque: 10% de desconto - à vista no cartão: 5% de desconto -
em até 2x no cartão: preço formal - 3x ou mais no cartão: 20% de juros '''

                          # calculo de taxa de juros
from time import  sleep
#                            ENTRADA DO VALOR DA MERCADORIA
compra = float(input("Valor presente: ".upper()).strip())
#                           PRINCIPAIS VARIÁVEIS  DO SISTEMA
pagamento = [1, 2, 3, 4]
r_taxa_juros = float(2.00) # Ao mês
a_vista = (compra / 100) * 90
a_vista_card = (compra / 100) * 95
card = (compra / 2)
parcelamento = 4
opcao = 5  # controle para while
p_valor_mercadoria = compra # Valor para calculo de Juros



print('\033[1;35m'+'programa de calculo de desconto e  pagamento.'.upper() + '\033[m')


# 1                                          WHILE PARA A ESCOLHA DO MENU
#                                       FALTA CONFIGURAR A OPÇÃO DE ERRO PARA LETRAS
while (opcao >=5 or opcao == 0 ):
    print('''\033[1;34mdigite a opção de pagamento do cliente:
    [ 1 ] A Vista com 10% de Desconto
    [ 2 ] A vista no Cartão de Crédito
    [ 3 ] Pagamento no Cartão em 2 x com Preço da Etiqueta
    [ 4 ] Pagamento no Cartão Parcelado acima de 3X com Juros de 2% am.\033[m''')
    opcao += 1
    opcao = int(input('\033[1;35m'+'Digite a opcão de pagamento: \033[m'.upper()))#.isdigit())
    if opcao >= 5:
        print('\033[1;36m'+'Opcão errada, escolha somente os Numeros do menu\033[m'.upper())
    elif opcao == str(''):
        print('\033[1;36m' + 'Opcão errada, escolha somente os Numeros do menu\033[m'.upper())
#                                             FIM DO LOOP WHILE

print('\033[1;36m' + '*.' * 15 + '\033[m')
print('Estamos processando seu pedido'.upper())
sleep(1)
#                                    IF da  ESCOLHA DA FORMA DE PAGAMENTO
if opcao == 1:
    print(' Pagamento A vista em dinheiro com 10% de desconto, o valor a pagar é: {:.2f} €'.format(a_vista))
elif opcao == 2:
    print(' Pagamento a vista com Cartão, com 5% de desconto, o valor a pagar é: {:.2f} €'.format(a_vista_card))
elif opcao == 3:
    print('Pagamento parcelado no cartão em 2x com preço da etiqueta {:.2f} €'.format(card))


#                             Inicio das Condicionais do calculo do JUROS
elif opcao == 4:
    print('Estamos processando o calculo das prestação'.upper())
    sleep(1)
    n_prestacao = input("Quantidade de parcelas: ".upper()).strip()  # quantidade de parcelas
    t_quantidade_de_prestacao = n_prestacao

#if (p_valor_mercadoria.isdigit() and r_taxa_juros.is_integer()
#   and n_prestacao.isdigit() and t_quantidade_de_prestacao.isdigit()):

    p = float(p_valor_mercadoria)
    r = float(r_taxa_juros) / 100
    n = float(n_prestacao)
    t = float(t_quantidade_de_prestacao)
    a = p * (1 + r / n) ** (t * n)
    valor_parcela = float( a / n )
                              # inicio das impressões

    print("Valor da Compra: {:.0f} ".format(p))
    print('Taxa de Juros ao Mês: {:.2f} €'.format(r_taxa_juros))
    print('Quantidade de Parcelas Escolhidas: {:.0f} €'.format(n))
    print('Total do Parcelamento com Juros: {:.2f} €'.format(a))
    print("Valor total a pagar por Mês:{:.2f} €".format(valor_parcela))

#else:
# print("Um ou mais valores informados são inválidos.")
print('\033[1;36m' + '*.' * 15 + '\033[m')
