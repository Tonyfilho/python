'''CORREÇÃO DO EXERCÍCIO'''

salario = float(input('Digite o Sálario do Funcionario €: '))
if salario <= 1250:
    salario_novo = (salario * 15 / 100)
else:
    salario = (salario * 10 / 100)
print('Seu novo Sálario é : {}'.format(salario))


