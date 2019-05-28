'''NESTE EXERCÍCIO ALÉM DE USARMOS O FOR USAMOS TB A CRIANÇÃO DE UMA FUNÇÃO CONTADORA'''
from time import sleep
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def contadora_2(x):
    for i in lista:
        print(i)
        sleep(1)


contadora_2(lista)
print('\033[1;35m'+'boommmmmm'.upper()+'\033[m')
sleep(1)
print('\033[1;34m'+'boommmmmmmmmmmm'.upper()+'\033[m')