'''Estaremos estudando ESTRUTURA SEGUENCIAIS CONDICIONAIS 1º PARTE'''

'''Estaremos estudando o IF e o ELSE'''

'''IF como estrutura simples '''
'''ELSE como estrutura composta'''
# Vejamos os exemplos abaixo

tempo = int(input('Que ano é o seu carro: '))
if tempo >= 2017:
    print('Parabéns, seu carro é Novo!')
else:
    print('Lamento, mas está  na hora de trocar seu carro! ')
print('***FIM***')


'''Ou seja temo uma CONDICIONAL COMPOSTA, onde s o ano do carro for maior e 
igual 2017 entraremos no IF
se for menor ao ano 2017 ele entrar no ELSE, mas NUNCA as 2 CONDIÇÕES'''

# DA FORMA SIMPLIFICADA PODEMOS ESCREVER ASSIM
if tempo >= 2017: print('Parabéns, o seu carro é Novo ')
else:print('Lamento, mas está  na hora de trocar seu carro! ')
print('***fim***')

# ou mais simplificada ainda
print('Parabéns, o seu carro é Novo 'if tempo >=2017 else 'Lamento, mas está  na hora de trocar seu carro!')
print('***fim***')

'''Isto chamamos de IF SIMPLIFICADO, no PYTHON não existe OPERADOR TERNARIO, que em outras
liguagens é parecido com isto'''