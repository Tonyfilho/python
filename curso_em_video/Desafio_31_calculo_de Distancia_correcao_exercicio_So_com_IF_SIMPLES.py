'''esta é a correção usando somenteo o IF sem o ELSE'''

from time import sleep
distancia = float(input('Digite a Distância da sua Viagem: '))
print('Sua Viagem terá {:.0f} KM Percorridos'.format(distancia))
print('PROCESSANDO......Tem um Burro me Olhando............')
sleep(3)
print('-=-' * 15)
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('A sua Passagem custa: {:.2f} Euros'.format(preco))
print('-=-' * 15)