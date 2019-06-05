'''correção do EXERCÍCIO 53 conforme o video'''
frase = str(input('Digite uma frase: ')).upper().strip()
palavra = frase.split() #Vai transformar a frase em uma LISTA
junto = ''.join(palavra) # demos um JOIN Sem ESPAÇO, ele juntou nossa LISTA
inverso = ''# faremos VAZIO, para que seja preenchido com com laço FOR
for itens in range(len(junto) -1, -1, -1):# (-1) ele desconsidera o ultimo espaço da string,
    # (-1)Vai até a primeira LETRA, (-1) Com passo NEGATIVO, ou seja de traz para frente.
    inverso += junto[itens]
if junto == inverso:
    print('Isto é um Palíndromo')
else:
    print('Isto não é uma Palíndromo')

print(junto, inverso)






