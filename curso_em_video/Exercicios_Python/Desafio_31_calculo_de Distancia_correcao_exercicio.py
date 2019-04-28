'''esta é a correção conforme a aula 31'''
from  time import sleep
distancia = float(input('Qual a Distância da sua Viagem: '))
print('A Sua Viagem tem {:.2f}KM de Distância.'.format(distancia))
print('/*/' * 15)
print('PROCESSANDO..... Tem um Burro olhando para mim....')
sleep(2)
if distancia <= 200:
    preco = 200 * 0.50

else:
    preco = 200 * 0.45
print('/*/' * 15)
print('Seu preço da sua Viagem será :{:.2f}' .format(preco))

