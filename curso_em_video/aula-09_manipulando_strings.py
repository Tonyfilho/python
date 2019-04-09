'''estaremos manipulando uma strings'''

'''toda STRING vai para memoria dividida por letra e espaço, e isto leva um INDICES, c'''

# fatiamento de strings

frase = 'Curso em Video Python'

'''se escreveremos assim frase[9], ele vai pegar somente o ITEM do INDICE 9 dentro da VARIAVEL FRASE, lembrando que sempre
precisa passar + 1, se termina no indicide 20, caso queiramos pega-lo temos que  ir ate o 21 '''
frase[9] #vai inciar no INDICE 9
frase[9:14] #vai iniciar no INDICE 9 ( V e vai ate o 14 que o O)
# ficando "VIDE0"
frase[9:21]# vai iniciar no indice (9 V e vai ate o 21 que é o N)
# ficando "VIDE0 PYTHON"
frase[9:21:2] # vai iniciar um FATIAMENTO DE indice 9 V e vai até o 21 que é o N, PULANDO 2 em 2 casa
#ficando "VDOPTO
frase[:5] # que dizer que vai do 0 C até o 5 que é O, PODEMOS FAZER ASSIM
frase[0:5]# é a mesma coisa que o exemplo acima.
'''OBS: Quando OMITIMOS só pondo os : ele entende que é para COMEÇAR DO 0(ZERO)'''
#ficando "CURSO"
frase[15:]# quer dizer que vai começar no indice 15 o P e vai até o final que é o N
'''Caso não saiba o final da STRING ESTA É A FORMA DE FATIAR e ir até o final dela.'''
#ficando "PYTHON"
frase[9::3]# vai iniciar no 9 o V, vai até o fim que é o :, PULANDO de 3 em 3
#ficando VEPH