'''Faremos um programa de media escolar'''
n1 = float(input('Digite a sua 1º nota: '))
n2 = float(input('Digite a sua 2º Nota: '))
media = (n1 + n2 ) / 2
print('Sua média É: {:.2f}'.format(media))
print('Sua media é boa 'if media >= 8 else'Sua média não é boa. Vai estudar BURRO.')

#ou assim

if media >= 8:
    print('Sua media é boa'.format(media))

else:
    print('Sua média é uma B... vai estudar BURRO'.format(media))


