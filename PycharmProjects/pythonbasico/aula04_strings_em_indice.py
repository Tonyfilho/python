'''Falaremos  OPERAÇÕES DE STRINGs e Indice'''

frase = 'Ola, esta é uma STRING'

'''Se formos em FRASE de dermos um PONTO apos veremos varios
metados e paramentros '''

print(frase.lower()) #Aqui deixamos todos as letras dentro da VARIÀVEL em minuscula
# ola esta é uma string
#OBs.: Ele não converteu a STRING, mas deixou somente o que imprimimos em MINUSCULO

'''OBS.: a STRING não  é uma lista , questão de INDICE ela se 
comporta igual, porém diversos outro metados são direrentes'''

frase_separada = frase.split(',')
print(frase_separada) #ela transforma nossa STRING em uma LISTA e
#separa da forma que colocarmos, olhe que pediremos para fazer isto
#pela VIRGULA ,olhe  a baixo o que imprimimos um lista com 2 itens
# ['Ola', ' esta é uma STRING']

## CONCATENADO VARIÁVEIS
frase_nova = frase + ' "Isto não estava na variável" '
print(frase_nova)
