n_digitado = int(input('Digite um numero: '))
somador = 0
contador = 0
# começo do laço FOR
for itens in range(0,  n_digitado+1, 2):
    somador += itens
    contador += 1



print('Total de numeros Pares contados são: {}, com a soma total de: {}'.format(contador,somador))