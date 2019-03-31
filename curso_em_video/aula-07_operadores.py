'''aula 7 SUBTRAÇÃO'''

'''ORDEM DE PRECEDENCIA'''
# 1º PARENTESES ()
# 2º ** POTENCIAS
# 3º FAZ QUE APARECER 1º * MULTIPLICAÇÃO, / DIVISÃO, // DIVISÃO INTEIRA, % RESTO DA DIVISÃO, MODULO
# 4º + ADIÇÃO E - SUBTRAÇÃO, QUEM APARECER PRIMEIRO


n1 = int(input('Digite o 1º numero: '))
n2 = int(input('Digite o 2º numero: '))
menos = n2 - n1
mais = n2 + n1
mult = n2 * n1
div = n2 / n1
div_m = n2 // n1
expo = n2 ** n1

#para quebra de linha \N
# para linha INTEIRA ,END='vazio' ou algum sinal que será impresso.


print('A Subtração é:{}, \nA Soma é:{}, \nA Multiplicação é:{},'.format(menos, mais, mult))
print('A Divisão é:{}, A Divisão Modulo é:{:3}, A Expoentização é:{:4}'.format(div, div_m, expo))
# A Divisão Modulo é:{:.3f} este :3 faz com que haja apenas 3 casas de numeros flutuantes depois do "."
# A Expoentização é:{:.4f}' este :4 faz com que haja apenas 4 casas de numeros flutuantes depois do "."

print('A Subtração é:{}, A Soma é:{}, A Multiplicação é:{},'.format(menos, mais, mult), end='')
print('A Divisão é:{}, A Divisão Modulo é:{:.3f}, A Expoentização é:{:.4f}'.format(div, div_m, expo))
# colocamos o END='' desta forma fica tudo impresso na mesma linha.
