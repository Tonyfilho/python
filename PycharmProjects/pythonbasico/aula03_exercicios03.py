'''Nesta Aula faremos conforma aprendemos, fazendo um cod mais enchuto'''
# requisitos minimos : idade 18 anos, altura 1.70, peso 60 kilos


nome = input('Digite seu nome:')
endereco = input('Digite seu endereço:')
idade = int (input('Digite sua Idade:'))
altura = float (input('Digite sua Altura:'))
peso = float (input('Digite seu Peso:'))

if idade >= 18  and altura >= 1.70 and peso >= 60:
    print('Aprovado!!!')
else:
    print('Reprovado Sabão de Mula')
