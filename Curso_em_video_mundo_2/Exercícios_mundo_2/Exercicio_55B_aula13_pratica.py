mais_velho = 0
mais_novo = 0
for itens in range(1, 5+1):
    idade = int(input('Digite sua idade'))
    if itens == 1:
        if idade > mais_novo > mais_velho:
            mais_novo = idade
            mais_velho = idade
    if idade > mais_velho:
        mais_velho = idade
    else:
#       if mais_novo > idade:
        mais_novo = idade
print('O mais venho tem {} de idade' .format(mais_velho))
print('O mais novo tem, {} de idade' .format(mais_novo))
