'''          WHILE COM VARIÁVEL DE CONTROLE'''

'''Aqui usamos o WHILE para criar um loop de um MENU onde a pessoa só pode escoher 1 das 
opções dada. Caso contrario o menu volta para o inicio'''


controle = 4  # a variável recebe um Valor
while (controle >= 4) or (controle == str):
    print('''[ 1 ] Pagar\n[ 2 ] Receber\n[ 3 ] Consultar''')
    controle = int(input('Digite 1 das opções acima'))
    if controle >= 4:
        print('\033[1;34m'+'Opção errada, tente novamente.'.upper() + '\033[m')

print('Estemos processando seu pedido'.upper())

