'''faremos a resolução conforme aula do curso'''

nun = int(input('Digite um Numero: '))
cont = 0 # Var contadora
for item in range(1, nun +1):
    if nun % item == 0:
        print('\033[1;33m'+ '{}'.format(item) + '\033[m', end=(''))
        cont += 1
    else:
        print('\033[1;31m' + '{}'.format(item)+ '\033[m', end=(''))
print('\nO numero {} é divisível {}X' .format(nun, cont))
if cont == 2:
    print('Este Numero {0} é primo, ser divisível por 1 e por {0}' .format(nun))
else:
    print('Este numero {} não é primo, pois é divisível por mais de 2X, com total de  {}X'.format(nun, cont))