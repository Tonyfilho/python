'''desafio 23 , faço  um programa que  leia um numero de 0 ha 9999 e mostre na tela  cada um dos digito separados
ex. 1934
unidade é: 4
dezena é: 3
centena é: 9
milhar é: 1
tenta fazer por STRING E POR MATEMATICA

'''

numero = int(input('Digite 1 numero: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f'Unidade é: {u}, \nDezena é: {d}, \nCentena é: {c}, \nMilhar é: {m}')