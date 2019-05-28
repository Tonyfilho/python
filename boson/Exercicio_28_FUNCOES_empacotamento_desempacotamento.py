''' NESTA AULA ESTUDAREMOS EMPACOTAMENTO E DESEMPACOTAMENTO, PARÂMENTROS EM FUNÇÕES'''

'''Vamos fazer o o exemplo a baixo '''
def listar_itens(x, y, z, w):
    print(x, y, z, w)

lista = [1, 2, 3, 4, ]
# listar_itens(lista) OBS: se ecrevermos desta forma , ele vai dar erro, visto que a LISTA é visto como 1 ITEM
# .somente faltando , termos o X, Y e o Z
# se colocarmos o " * " FAREMOS O DESEMPACOTAMENTO DA LISTA, e com isto o ERRO some.
listar_itens(*lista) # DESTA FORMA " * " , ELE DESEMPACOTA NOSSA  LISTA

'''                               OUTRO EXEMPLO DE DESEMPACOTAMENTO    '''

'''                            , Agora colocamos 1 numero infinito de ARGUMENTOS   '''

def listar_itens_2(* args): # desta forma colocamos 1 NUMERO infinito de argumentos
    print(args)
lista_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listar_itens_2(*lista_2)

'''                               OUTRO EXEMPLO agora de EMPACOTAMENTO    '''

def empacotar_itens(* args): # " * " COLOCANDO O ASTERISCO. o NOME pode ser qualquer nome, o PADRÃO NESTE CASO é o ARGS
    soma = 0
    for i in range(0, len(args)):
        soma += args[i]
    return soma
a = int(input('digite o 1º numero: '.upper().strip()))
b = int(input('digite o 2º numero: '.upper().strip()))
c = int(input('Digite o 3º numero: '.upper().strip()))

empacotar_itens(a, b, c)

resultado = empacotar_itens(a, b, c)
print(resultado)



