'''Podemos fazer uma FUNÇÃO SEM RETORNO E ARGUMENTOS
'''

i = 0

def imprime_oi ():
    print('Oi')
#esta função fica imprimindo o "OI"
#podemos dar um WHILE
# Nos paramentros posso passar qualquer tipo
# de OBJETO , lista, tupla, objetos criados, e funções.

'''Vamos dar um exemplo de função de retorna BOOLEANO'''


def tem_sete_letras (argumento):# Posso chamar de qualquer coisa
#Poderia ser qualquer coleção
    if len(argumento) == 7:
        return True
    else:
        return False
#Feita a FUNçÂO  vamos testa-las
print( tem_sete_letras('tem sete letras?''Linha 23'))

'''False'''

print(tem_sete_letras('Linha27'))
'''
True
'''
# Como é uma função BOOLEANA podemo por ela
# dentro do IF:
if tem_sete_letras('linha33'):
    print('Tem 7 letras')
else:
    print('Não tem 7 letras')
# Algo legal no PYTHON como não preciso especificar
# o tipo  de argumento, posso passar qualquer coisa,
# o o exemplo abaixo, passaremos uma lista que CONTEM 7 NUMEROS
# Pode ser uma dicionarios "DICT" ou conjunto "SET"

if tem_sete_letras([1,2,3,4,5,6,7]):
    print('realmente tem sete letras na linha 43')
else:
    print('Não tem  7 letras')

#podemo passar qualquer conjunto de dados ou coleções,
# listas , string, dicionarios, tublas e outros.

'''Função é quando temos um RETURN
   METADO é quando não precisos por o RETURN, ouseja
   vc passa algo e execultado e não temos pedimos os 
   retorno'''


