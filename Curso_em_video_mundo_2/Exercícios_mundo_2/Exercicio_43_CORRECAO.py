'''Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa
Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo: - IMC abaixo de 18,5: Abaixo do Peso -
Entre 18,5 e 25: Peso Ideal - 25 até 30: Sobrepeso - 30 até 40: Obesidade - Acima de 40: Obesidade Mórbida'''

'''Esta  é a correção  da aula 43, com o codigo igual ao do video'''

peso = float(input('Qual o seu peso?  (Kg)'.upper().strip()))
altura = float(input('qual é a sua altura?  (m)'.upper().strip()))
imc = peso / (altura ** 2)
print('\033[1;35m' + '*0* ' * 15 + '\033[m')
print('o IMC dessa pessoa é de {:.2f}, isto é, '.format(imc).upper(), end='')

if imc < 18.5:
    print('abaixo do peso'.upper())
elif 18.50 <= imc < 25:  # FORMA SIMPLIFICADA DO IF SEM O "AND"
    print('peso ideal'.upper())
elif 25 <= imc < 30:
    print('sobrepeso'.upper())
elif 30 <= imc < 40:
    print('obesidade'.upper())
else:
    print('obesidade morbita'.upper())
print('\033[1;35m' + '*0* ' * 15 + '\033[m')



