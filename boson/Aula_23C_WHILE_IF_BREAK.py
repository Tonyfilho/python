'''WHILE COM BREAK'''

''' A declaração BREAK termina com o LOOP atual e processegue a execução na PRÓXIMA declaração após o LOOP'''
''' O uso mais comum é quando alguma CONDIÇÃO EXETERNA é disparada e requer a saída imediata do LOOP'''
''' O comando BREAK pode ser usado tanto em LOOPS WHILES quantos em LOOP FOR.'''


while_break = 20
while (while_break > 0):
    print('O valor de WHILE_BREAK é: {}'.format(while_break))
    while_break -= 1
    if while_break == 11:
        break
print('fim do programa, loop interrompido no valor {}'.upper().format(while_break))