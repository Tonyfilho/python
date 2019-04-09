'''faça um programa que leia e abra um audio em MP3'''

'''o Harcking é usar MODULOS do PYPI, procure '''

import pygame
pygame.init() #Este é init do Pygame, temos que sempre iniciar a biblioteca assim.
pygame.mixer.music.load('02.mp3') #tenho que carregar o MIXER,MUSIC.LOAD
pygame.mixer.music.play()# este é torcar..
pygame.event.wait() #para esperar até o fim da musica
