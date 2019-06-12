'''                                                              MÓDULOS'''

'''Um MÓDULO é uma ARQUIVO que pode ser usado como CONTEINER para FUNÇÕES, CLASSES E VARIÁVEIS,de modo a reaproveita-las
quando necessário, importando o MÓDULO com o comando IMPORT'''

'''OBS: Os MÒDULOS são aqrquivos com extenção.PY'''

'''                                 NESTA AULA APRENDEREMOS A CRIAR NOSSO PROPRIOS MODULOS'''

'''                                   EXEMPLO:'''

'''Vamos trabalhar com 2 arquivos; 1 será o programa principal, e o outro um ARQUIVO de nome MODFUNÇÕES.PY no qual 
declararemos algumas funções que serão importadas e utilizadas no módulo principal'''

## MODULO DE FUNÇÕES VARIADAS

## MODULO PRINCIPAL
import Exercicio_31_MODULO_modulacoes  #FIZEMOS A IMPORTAÇÃO DO NOSSO MODULO CRIADO POR NÓS

Exercicio_31_MODULO_modulacoes.mensagens()  # ESTAMOS CHAMANDO NOSSO MODULO com FUNÇÃO MENSAGENS

n_1= int(input('Digite um numero inteiro: ')) #VAR DE NUMERO PARA CALCULOS
print('calculando o fatorial do número: ')
fat = Exercicio_31_MODULO_modulacoes.fatorial(n_1) # CHAMANDO A FUNÇÃO FATORIAL DO MODULO
print('O Fatorial do Nº {} é : {}'.format(n_1, fat))

fib = Exercicio_31_MODULO_modulacoes.fibonacci(n_1) # CHAMANDO A FUNÇÃO FIBONACCI DO MÓDULO
print('O Fibonacci do N {} é : {}'.format(n_1, fib))

'''                                               Onde se localizam os Módulos?'''
'''Quando um Módulo é iportado, o INTERPRETADOR procura 1º por um MÓDULO PADRÃO com o nome do módulo. Se
NENHUM for encontrado, ele produrará por um ARQUIVO com nome do Módulo de EXTENSÃO.PY em uma lista de DIRETÓRIOS
presentes na VARIÁVEL SYS.PATH, a qual é inicializada do seguintes locais:'''

'''Diretório que contém o SCRIPT de entrada, ou diretório ATUAL se nenhum arquivo for especiicado.'''

'''PYTHONPATH, que é uma lista de nomes de diretórios com a mesma sintaxes dao SHELL PATH'''

'''O Local PADRÃO, dependente da instalação'''

## LISTA DE COMANDO PARA EXECULTAR OS SEGUINTES COMANDO NO SHELL DO PYTHON

import sys  ##aqui ele fala se o MODULO é BUILT-IN ou BUILT-OUT
print(sys)

'''Podemos acrescentar mais diretórios a variável SYS.PATH, usando a FUNÇÃO append() como segue'''

# sys.path.append('/home/tony/documents/git') # no caso do linux para ser execultado no SHELL