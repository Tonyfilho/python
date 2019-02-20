''''Aqui veremos o NOT ou seja ele tranforma TUDO QUE FOR
VERDADEIRO E FALSO E TUDO QUE DOR FALSO EM VERDADEIRO'''


#podemos  da  o exemplo
# se deremos um print com True veremos

print(True) #ou seja aqui aparecerá True na tela
print(not True) #Aqui aparecerá FALSE na tela
print(not False) #Aqui aparecerá TRUE na tela

'''ou seja quando usamos o NOT invertemos os valores BOOLEAN'''

nome = 'Tony'
idade = '50'

if idade == 50:
    print('Você tem 50 anos')
else:
    print('Você não 50 anos')


if not idade == 50: # aqui o NOT vai fazer o programa ir para linha 26
    print('Você NÃO tem 50 anos')
else:
    print('Voce SÓ Tem, Por causa do NOT')

'''Vamos dar um outro exemplo'''

if True:
    print('Entra o IF TRUE')
else:
    print('Se não for,  ELSE ele apareserá aqui linha 33')

if not True:
    print('Entra IF TRUE linha 36')
else:
    print('Entra Else da linha 38')

    











