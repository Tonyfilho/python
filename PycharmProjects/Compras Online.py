print('Opções de Notebooks: \n1 = Comprar Acer Aspire A315-53G. 530.00€\n2 = Comprar Omen 332-AGHP. 1299.00€ \n3 = Comprar Alienware Area51. 2000.00€\n')
notes = input('Escolha um Notebook com diferentes configs  para comprar. Você tem 2k euros.')

if notes == '1':
    print('Parabens!!! Você escolheu um note com sabedoria!!! Lembre-se seu filho tirou boa nota a matemático por isso você comprou este note.')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Sua carteira tem:', 530-2000)
elif notes == '2':
    print('Ok nada mal. até que é um note bom, mas lembre-se você só comprou isso para ter um bom note.')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Sua carteira tem:', 1299-2000)
elif notes == '3':
    print('PARABÉNS!!!!! VOCÊ ACABA DE GASTAR TODAS AS SUAS ECONOMIAS!!!!!!! SEU BURRO!!!!')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Sua carteira tem:', 2000-2000, '!!!!!!!')
else:
    print('Seu filho não mereceu nada!!! Por isso ensine ele a ser um merecedor!!!')
