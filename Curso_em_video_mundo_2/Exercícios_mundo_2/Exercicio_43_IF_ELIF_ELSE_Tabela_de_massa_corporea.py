'''Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa
Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo: - IMC abaixo de 18,5: Abaixo do Peso -
Entre 18,5 e 25: Peso Ideal - 25 até 30: Sobrepeso - 30 até 40: Obesidade - Acima de 40: Obesidade Mórbida'''


print('\033[1;34m' + 'programa de calculo de massa corpórea: '.upper() + '\033[m')
print('\033[1;35m' + 'digite os valores pedido pelo programa: '.upper()+ '\033[m')
indice_altura = float(input('digite o valor de altura em metros "Ex: 1.80": '.upper()))
indice_peso = float(input('digite o seu peso em quilos. "Ex: 80": '.upper()))
imc = indice_peso / (indice_altura ** 2)
if imc <= 18.50:
    print('Vai comer sua caveira, seu imc é: {:.2f}'.format(imc).upper())
elif imc > 18.50 and imc <= 25:
    print('Seu peso está ótimo, fique esperto para não ficar gordo, seu imc é: {:.2f}' .format(imc).upper())
else:
    print('Vai chupeta de baleiaaaaa, fecha a boca sem fimmmmm, seu imc é: {:.2f}'.format(imc).upper())
