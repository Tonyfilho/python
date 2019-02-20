''''faremos uma menu'''


print('Opções do menu:\n1 = frango\n2 = bife\n3 = costeletas\n4 = churrasco\n')

opcao = input('Escolha um dos menus acima:')

if opcao == '1':  # usamos 1 IF e depois passaremos a usar o ELSEIF
    print('frango')
elif opcao == '2': # ELIF é = ELSE IF  ou seja  o Se Não
    print('bife')
elif opcao == '3':
    print('costeletas')
elif opcao == '4':
    print('churrasco')
else: # Neste caso TEMOS que terminar com o ELSE caso seja uma escolha fora das do menu
    print('Escolha errada, fv volte ao menu:')
'''Ou seja  ele vai comparar as opções de 1 a 4, caso não
seja NENHUMA delas e cai para ELSE eo ELSE NÂO faz comparações
se TUDO acima deu 
'''

'''Quais as principais diferença do IF e ELIF ??'''
'''É que ele entra no IF, se for VERDADEIRO O PROGRAMA PÁRA
caso for FALSO o programa continua ou seja deu verdadeiro no IF finaliza, 
SENÂO SE ele continua executando '''


