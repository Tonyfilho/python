'''                                                     FOR'''
'''O loop FOR em python pode ITERAR pelos itens de qualquer SEGUÊNCIA, como uma LISTA ou STRING'''

'''   SINTAXE:'''

'''FOR variável in SEGUENCIA:''' # ACHAMAMOS DE VARIÁL INTERADORA OU INTERANTE, AQUE SE REALCIONA COM O FOR
'''     COMANDOS'''

'''                                                EXEMPLOS'''

variavel_for = 'string'
for i in variavel_for: # O LOOP FOR vai desmembrar a STRING , ficando letra sobre letras
    print(i)

frutas = ['laranja', 'morango', 'guaraná','açaí']
for i in frutas:
    print(frutas[2]) # O LOOP FOR vai imprimir o ITEM da posição 2, na quantidade que existe na LISTA
    print('Fruta : {}'.format(i)) # o LOOP FOR imprimirar CADA ITEM da LISTA

'''                                     Loop FOR como contador'''
