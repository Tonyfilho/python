'''Nesta Aula faremos conforma aprendemos, fazendo um cod mais enchuto'''
# requisitos minimos : idade 18 anos, altura 1.70, peso 60 kilos

input('Digite seus dados para seleção do exercito, Favor aperte o ENTER para começar:')

nome = input('Digite seu Nome Completo:')
idade = int(input('Escreva sua Idade:'))
altura = float(input('Escreva sua Altura em Metros'))
peso = float(input('Escreva seu Peso:'))

if idade >= 18 and altura >= 1.70 and peso >= 60 :
    print('Você foi Aprovado:')
else:
    print('Infelizmente voce foi Reprovado')

print('Seu Nome:',nome, 'Sua Idade:',idade, 'Sua Altura:',altura, 'Seu Peso:',peso )

