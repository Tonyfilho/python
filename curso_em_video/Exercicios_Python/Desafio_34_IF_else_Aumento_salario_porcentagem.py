'''Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do
seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais,
o aumento é de 15%.'''

sal  = float(input('Digite seu Sálario: '))
aumento_baixo = sal * 0.15
aumento_alto = sal * 0.10
if sal <= 1250.00:
    salario_novo = sal + aumento_baixo
else:
    salario_novo = sal + aumento_alto
print('Seu Aumento de Sálario foi: {:.2f}'.format(salario_novo))
