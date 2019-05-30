'''AULA 48 Faça um programa que calcule a soma entre todos os números que são múltiplos de três e
 que se encontram no intervalo de 1 até 500.'''

soma = 0 # Var SOMA  é para receber a soma do numeros, ele sempre começa com ZERO
contador = 0 # Var CONTADOR é para receber a CONTAGEM dos numeros, ela sempre começa com zero
numero = int(input('digite uma numero: '.upper().strip()))

for itens in range(1, numero+1, 2): # LAÇO DE SEPARAÇÃO DE NUMEROS IMPARES
    if itens % 3 == 0:  # IF PARA VERIFICAÇÃO SE SÃO DIVISÍVEIS E MULTIPLOS DE 3
        soma += itens  #  SOMADORA OBS: Ou escrevemos SIMPLIFICADO ou assim: "soma = soma + itens"
        contador += 1  #  CONTADORA OBS: Ou escrevemos SIMPLIFICADO ou assim: "contador = contador + 1"



print('\033[1;34m' + ' O numero {}, tem {} numeros IMPARES multiplos de 3, com total  somado de:  '
                     '{}'.format(numero, contador, soma) + '\033[m')

