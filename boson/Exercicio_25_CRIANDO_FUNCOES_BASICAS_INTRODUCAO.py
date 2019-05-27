'''                                                FUNÇÕES - INTRODUÇÃO'''
'''FUNÇÕES: Uma função é um agrupamento de instruções que podem ser executadas MAIS de  uma VEZ em um programa.'''

'''É possível passar a uma função parâmentros de  entrada,que podem ser diferente  a cada vez que a  função é EXECUDADA'''

''' OBS: Quando chamamos uma função, falamos que EVOCAMOS a função'''

'''                              FINALIDADE DAS FUNÇÕES:'''

'''Básicamente, CRIAMOS FUNÇÕES POR 2 PRINCIPAIS MOTIVOS:
1º REUTILIZAÇÃO DE CÓDIGO
2º MODULARIZAÇÃO , ou seja dividir o codigo em menores partes, com isto resolvermos BUGs do nosso codigo'''

'''                            TIPO DE FUNÇÕES:'''

'''Há 2 tipos de FUNÇÕES em Python:
FUNÇÕES internas (BUITIN) EX. a função PRINT

FUNÇÕES definidas pelo USUÁRIO'''

'''NOrmalmente criamos FUNÇÕES de algo que não temos, ou seja se precisarmos execultar algo que não  exista no PYTHON
então criamos uma  FUNÇÃO DEFINIDA'''

'''                             CRIANDO FUNÇÕES EM PYTHON'''

# Definimos uma nova FUNÇÃO usando a instrução DEF, de acordo com a SINTAXE a seguir:

# def <nome_da_funcao>(argumentos): OBS: MUITAS FUNÇÕES NÃO RECEBEM ARGUMENTOS,  elas só execultam tarefas
#   <instruções>

'''                  EXEMPLO: Função para exibir uma mensagem'''

def mensagem():
    print('Aula sobre criação de função'.upper())

mensagem() # DESTA FORMA INVOCAMOS A FUNÇÃO, OU CHAMAMOS ELA .

''' A instrução DEF cria uma OBJETO e atribui um nome a ELE'''




