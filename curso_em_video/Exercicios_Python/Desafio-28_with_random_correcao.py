'''esta é a correção do exercicio, ou seja igual ao do video'''

from random import randint
computador = randint(0, 5) #faz o programa escolher aleatoriamente 1 numero de 0 a 5
print('-*-' * 30)# Criamos uma separação
print('Vou escolher um Numero de 0 há 5. Adivinha qual é?: ')
print('-*-' * 30)
jogador = int(input('O Numero que escolhi é: ')) #O jogador eslhe o numero
if jogador == computador:
    print(f'Parabéns! Você acertou o Numero!: {jogador}')
else:
    print('Você errou! O Numero que do Computador é: {}, e o Numero escolhido foi: {}'.format(computador, jogador))



