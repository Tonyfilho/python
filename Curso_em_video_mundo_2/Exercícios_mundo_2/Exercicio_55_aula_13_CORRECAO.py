'''CORREÇÃO DA AULA 55 PELO VIDEO'''

mais_pesado = 0
menos_pesado = 0
'''OBS: Quando tivermos maior ou menor, temos que verificar sempre a 1ª OCORRÊNCIA OU o 1ª IF,
ou seja, ele vai ser o MAIOR E O MENOR, e depois do 2º IF que teremos MAIOR E MENOR'''
for itens in range(1, 5+1):
    peso = float(input('Digite o Peso da {}ª Pessoa: '.format(itens)))
    if itens == 1: # Aqui perguntamos quando o ITEM 1 do laço FOR == 1, ou seja quando digitarmos o 1º Item.
        mais_pesado = peso
        menos_pesado = peso
    else:
        if peso > mais_pesado:
            mais_pesado = peso
        if peso < menos_pesado:
            menos_pesado = peso

print('O maior preso lido foi: {:.2f}KG, o menor peso lido foi: {:.2f}KG'.format(mais_pesado, menos_pesado))


