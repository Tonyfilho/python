'''faça um progrma que  leia um ANGULO qualquer, e mostre
na tela o VALOR do SENO, COSSENO e TANGENTE de angulo

'''

'''o HARKERING deste exercicio é IMPORTAR BIBLIOTECAS 
NO pypi ou math
'''
import math
angulo = math.radians(float(input('Digite o Ângulo que vc quer saber: ')))
sen = math.sin(angulo)
cos = math.cos(angulo)
hip = math.tan(angulo)

print(f'O Angulo de: {angulo}', f'\ntem Seno de: {sen:.2f} Graus', f'\nTem Cosseno de: {cos:.2f} Graus', f'\nTem Tangente de: {hip:.2f} Graus')
