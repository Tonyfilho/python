''''                    Módulos-Básico
em termos gerais ,c ada arquivo de codigo fonte do Python
com extensão .PY é um módulo'''

'''Outros arquivos podem acessar  itens em uma módulo por meio da
importação de  módulo'''

'''Essa operação carrega um arquivo de codigo-fonte e dá acesso
ao seu conteúdo dentro do programa'''

### Para importar um arquivo e utilizar o seu conteudo em um
# programa, use a sintaxe a seguir:

# 1-0 import nome_modulo.py

### Para usar o conteudo de um modulo importado, use o nome
# do modul, seguido por um PONTO (.) e o nome do ATRIBUTO,
# VARIÁVEL ou METADO DESEJAVEL: EX

# a = nome_modulo.atributo


'''   Vamos ver nos exemplos a seguir:  usando  um MÓDULO já criado  1º:

a = 'abacaxi'
b = 'morango'
c = 'banana'
d = 'damasco'
e = 'laranja'
'''
### poderia ser uma listagem de funções matematicas ou outras
### vamos cria agora nosso programa principal que mostra qual fruta
# eu gosto de saborear depois das refeições, para isto poderiamos
# repetir e colocar todas as variaveis que colocamos no nosso
# modulo ou IMPORTA LAS  de um ARQUIVO que já tem as variaveis
# , usando o importe.nome_do_modulo.py

#OBS: o modulo tem que estar no mesmo diretorio do programa.
# Usamos o print, mas poderia ser qualquer outro
# e concatemos com a STRING e no final colocamos o
# PONTO(.)e o nome da VARIAVEL do modulo.
# lembrando que a variável se encontra no MODULO_FRUTA

import modulo_fruta

print('gosto de comer ' + modulo_fruta.b)

'''Sempre que precisarmos importar COMANDO, ARQUIVOS, VALORES e 
ATRIBUTOS, VARIAVEIS de outro arquivo do PYTHON , usaremos  o comando
IMPORT e poderemos usar varios modulos, um embaixo do outro e acessar
 as informações de modulo PONTO(.) nome da propriedade, atributo variavel etc.'''


















