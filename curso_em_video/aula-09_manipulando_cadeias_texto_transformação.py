''' De via de regra uma LISTA de string é IMUTÁVEL, mas poder transformada'''

'''conseguiremos muda-la atravez do METADOS'''

frase = 'Curso em Video Python'
frase2 ='   Aprenda Python   ' #colocamos os espaço no inicio e no fim para demostrarmos o ex. seguintes

#falaremos do METADO REPLACE, onde ele reloca  o conteudo da variavel
print(frase.replace('Python', 'Android')) #Onde ele vai substituir a paravra PYTHON por ANDROID
#Curso em Video Android
print(frase.upper()) #vai por toda a string em caixa alta
'''o UPPER ser um METADO precismo por ()'''
#CURSO EM VIDEO PYTHON
print(frase.lower()) # vai por toda a string em caixa baixa
'''o LOWER ser um METADO precismo por ()'''
#curso em video python

print(frase.capitalize())# coloca a 1º letra da string com caixa alta
#Curso em video python

print(frase.title()) # coloca as 1ªs letras de CADA palavra em caixa alta
#Curso Em Video Python

'''Usaremos a 2ª variável com espaço para podermos usar outros METADOS de transformação'''
print(frase2.strip())# ele remove todos os espaços inuteis, do inicio e do fim.
#Aprenda Python  sem os ESPAÇOS da string

print(frase2.rstrip()) #ele remove todos os espaços initeis da DIREITA
#  Aprenda Python

print(frase2.lstrip()) #ele remove todos os espaços initeis da ESQUERDA
#Aprenda Python
'''Muitas funções no python tem VARIAÇÕES R e L'''



