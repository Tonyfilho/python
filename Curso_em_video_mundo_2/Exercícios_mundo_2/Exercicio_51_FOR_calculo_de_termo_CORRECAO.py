'''FAREMOS A CORREÇÃO DO EXERCICIO 51, CONFORME  O VIDEO'''
termo = int(input('digite o termo: ').upper().strip())
razao = int(input('digite a razão: ').upper().strip())
decimo = termo + (11 - 1) * razao
for itens in range(termo, decimo, razao):
    print('{}'.format(itens),end='->')

