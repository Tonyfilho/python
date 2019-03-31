'''faça um algoritimo que leia o salario de  um funcionario e mostre seu
novo salario com aumento de 15% '''

salario = float(input('Digite o Seu Salário: '))
aumento = float(input('Digite o Aumento de Sálario: '))
salario_novo = salario + (salario * aumento / 100)

print(f'O Salário novo é: {salario_novo}')

