'''VIDEO 17 LISTA- PARTE02 METADO POP, SORT, REVERSE, MAPEAMENTO'''

'''criando LISTA, abre e fecha COCHETES e coloque os ITENS caso seja'''
lista = [50, 60, 80]  # Uma Lista vazia
lista_de_numeros = [0, 1, 2, 3, 4, 5]  # Lista com números
lista_bagunca = [3, 4, 5, 8, 1, 6]

lista_de_numeros[3] = 100 # TRIBUIMOS 0 NUMERO 100 NA POSIÇÃO 3, SUBTITUINDO O NUMERO DA POSIÇÃO 3 PELO 100 AUTOMATICAMENTE
print(lista_de_numeros)
print('\033[0;34m' + '*+*' * 10 + '\033[m')
lista_de_numeros[2:6] = [20, 30, 40, 50, 60]   # ATRIBUIMOS VARIOS E NOVOS NUMEROS NAS POSIÇÕES E ADCIONAMOS OUTROS A MAIS.
print(lista_de_numeros)
print('\033[0;34m' + '*+*' * 10 + '\033[m')
'''Podemos criar a LISTA LISTA2, com os elementos da LISTA INCREMENTADOS, usando o FOR para INTERARMOS ou fazer
COMPREENÇÃO somando + 1, '''

lista2 = [i + 1 for i in lista]  # desta forma CRIAMOS uma LISTA NOVA adcionamos 1 há mais para cada item da LISTA
print(lista2)
'''a LISTA2 foi CRIADA E INCREMENTADA, ou seja onde era 50, virou 51, 60 virou 61 e 80 virou 81, OU seja para 
cada item na VAR LISTA individualmene aplico uma operação e ARMAZENO isto em outra VARIÁVEL'''
print('\033[0;34m' + '*+*' * 10 + '\033[m')
'''OUtro exemplo usando POTENCIAÇÃO, onde  CRIAREMOS UMA NOVA VARIÁVEL E pegaremos os valores na POTENCIA 10 da 
VARIAVÉL CLONADA'''
lista3 = [i ** 10 for i in  lista]  # Passamos por POTêNCIA de 10
print(lista3)

lista4 = [i ** (1/2) for  i in lista3]  # Passamos por RAIZ QUADRADA
print(lista4)

print(len(lista4)) # DESCOBRIMOS  o tamanho da LISTA

'''TEMOS TB A OPERAÇÃO MAP,  QUE  É UM MAPEAMENTO que faz a mesma coisa que a INCREMENTO OU COMPREENÇÃO COM  o for
mas EM FUNÇÕES DO PYTHON '''
'''O MAP aplica uma função F a CADA ITEM da lista, tipo o for in,MAS SOMENTE COM FUNÇÕES, tipo raiz quadrada ou po
tenciação etc  '''
from math import sqrt
print(map(sqrt(),lista_de_numeros))  # EM CADA ITEM DA VARIÁVEL LISTA aplicaremos o MAP com FUNÇÃO RAIZ QUADRADA

