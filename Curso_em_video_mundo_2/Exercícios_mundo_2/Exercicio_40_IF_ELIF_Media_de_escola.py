'''Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
no final, de acordo com a média atingida: - Média abaixo de 5.0: REPROVADO - Média entre 5.0 e 6.9: RECUPERAÇÃO -
Média 7.0 ou superior: APROVADO'''

print('Este é um Programa de média escolar, Digite a suas 3 notas: '.upper())
nota_1 = float(input('Digite a 1º nota').upper())
nota_2 = float(input('Digite a 2º nota: ').upper())
nota_3 = float(input('Digite a 3º nota: ').upper())
media = (nota_1 + nota_2 + nota_3) / 3
if media >= 7:
    print('Parabens sua média é: {0:.2f}, você foi Aprovado! '.format(media).upper())
elif media >= 5 and media <= 5.9:
    print('sua média é: {0:.2f}, com esta média de: {0:.2f}, com está de recuperação.'.format(media).upper())
else:
    print('sua media é: {0:.2f}, com esta média  de: {0:.2f} você reprovou.'.format(media).upper())



