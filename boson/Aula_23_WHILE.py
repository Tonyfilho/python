'''loop com  WHILE quer dizer ENQUANTO'''

'''WHILE é Estruturas de repetição que  permite executar um bloco de código enquanto uma CONDIÇÃO de teste 
retornar VERDADEIRO'''

'''SINTASE'''
'''WHILE(condição):'''
'''   BLOCO DE CÓDIGOS'''
'''                                                EXEMPLO:'''
contador = 0
while (contador < 50):
    print('O valor de {} de contador'.format(contador))
    contador += 1 # FUNÇÃO DE incremento que adciona mais 1 para cada LOOP, É OBRIGATÓRIO
print('Fim do loop'.upper())
'''                                                EXEMPLO 2'''
'''                                       WHILE COM VARIÁVEL DE CONTROLE'''
controle = 4  # a variável recebe um Valor
while (controle >= 4):
    print('''[ 1 ] Pagar\n[ 2 ] Receber\n[ 3 ] Consultar\n[ 4 ] Sair''')
    controle = int(input('Digite 1 das opções acima'))
    print('\033[1;34m'+'Opção errada, tente novamente.'.upper() + '\033[m')

print('Estemos processando seu pedido'.upper())

'''                                                EXEMPLO 3'''
'''                                         WHILE COM BREAK'''

''' A declaração BREAK termina com o LOOP atual e processegue a execução na PRÓXIMA declaração após o LOOP'''
''' O uso mais comum é quando alguma CONDIÇÃO EXETERNA é disparada e requer a saída imediata do LOOP'''
''' O comando BREAK pode ser usado tanto em LOOPS WHILES quantos em LOOP FOR.'''


while_break = 20
while (while_break < 20):
    print('O valor de WHILE_BREAK é: {}'.format(while_break))
    while_break -= 1
    if while_break == 11:
        break
print('fim do programa'.upper())

