'''Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que
 forem pares. Se o valor digitado for ímpar, desconsidere-o.'''

#numero = int(input('Digite um Numero par'))
somador = 0
contador = 0
for itens in range(1, 6+1 ):
    recebe = int(input('Digite o {}º Numero:  '.format(itens)))
    if recebe % 2 == 0:
        somador += recebe
        contador += 1

print('A soma dos {} numeros pares são {} '.upper().format(contador, somador))

