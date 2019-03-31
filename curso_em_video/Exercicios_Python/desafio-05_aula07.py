'''faça um programa que  leia um numero INTEIRO
e mostra o sucessor e seu anterior'''

n1 = int(input('Digite um numero: '))
mostre_numero = n1
mostre_numero_ant = mostre_numero - 1
mostre_numero_Post = mostre_numero + 1


print('O numero Anterior é:{}, \nO numero Sucessor é:{}, \no numero Digitado é:{}'.format(mostre_numero_ant,mostre_numero_Post,mostre_numero))
