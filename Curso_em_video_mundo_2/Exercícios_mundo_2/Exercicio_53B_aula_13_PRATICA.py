'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços'''
'''                                    EXERCÍCIO DE PRATICA SEM VER A CORREÇÃO'''

palindromo = str(input('Digite aqui sua frase: '.upper()).upper().strip())

lista = palindromo.split()  # PODEMOS usar o JOIN p/v TRANSFORMAR EM UMA LISTA E DEPOIS RETIRAR OS ESPAÇOS DA LISTA COM O JOIN

junto_2 = ''.join(lista)  # PODEMOS USAR O JOIN NA LISTA PARA SUBSTITUIR OS ESPAÇO,POR SEM ESPAÇOS

junto = palindromo[::].replace(' ', '')  # OU PODEMOS FAZER ASSIM NA  PARA REMOVER OS ESPAÇOS DA str

inverso = ''

for itens in range(len(junto_2) -1, -1, -1):
    inverso = junto_2[itens]
if junto_2 == inverso:
    print('A palavra {} é  um Palidromo'.format(palindromo))
else:
    print(' A palavra {} não é um Palidromo'.format(palindromo))

#print(junto)
#print(junto_2)
#print(inverso)
