'''                                       TIPO DE ARQUIVOS : TEXTO SIMPLES E BINÁRIO'''

'''aRQUIVOS DE TEXTO(plantext) São um seguencia de estruturas de linha, que contén cada uma seguência de caracteres
, sem informações sobre formatação'''

'''Cada linha é termina com caractere especial de FIM DE  LINHA, EOL(End of Line). No geral, é o caractere newline"\n"
. Esse caractere finaliza a linha atual e diz ao interpretador que uma nova linha se inicia '''

'''1 Aquivo BÍNARIO é qualquer arquivo que não seja TXT, ou seja todos os demais tipos de aquivos, EX. MP3, planilhas.
 Word, excel, pdf, MP4 etc. Aquivos BÍNARIOS, somente pode ser processados para compreender a estrutura do arquivo.


'''

'''Estaremos nesta 1º Aula sobre aquivos, LER E ESCREVER somente nos arquivos simples ou TXT, e nas Aula 32 falaremos 
sobre ARQUIVOS BÍNARIOS, '''

'''                                        ABRINDO ARQUIVOS DE TEXTO COM PYTHON'''

''' 1 Arquivo é uma área no disco onde gravamos e de inde lemos dados '''
''' Podemos pensar em um arquivo de texto cmo sendo uma seguência de linhas'''
''' Para trabalharmos com arquivos no python usaremos o objeto "FILE" '''
''' Os objeto file contém MÉTADOS e ATRIBUTS que podem ser usados para coletar informações e manipular um ARQUIVO'''
''' Um OBJETO FILE possue um ATRIBUITO NOME ou CAMINHO do ARQUIVO, que é o nome do arquivo manipulado, e um ATRIBUITO MODO, que é o 
modo como o arquivo será LIDO ou ESCRITO'''
''' Para trabalhar com arquivos de texto precisamos :ABRIR, CHAMA-lo de modo apropriado(LEITURA/ESCRITA) E FECHAR O 
ARQUIVO'''

'''                    MODOS DE ACESSO A ARQUIVOS COM OPEN() '''

# r             SOMENTE LEITURA
# r+            LEITURA E ESCRITA
# w             ESCRITA APAGANDO (trocando) O CONTÉUDO EXISTENTE NO ARQUIVO
# W+            LEITURA E ESCRITA. O ARQUIVO É CRIADO, SE NÃO EXISTIR. SE EXISTIR É TROCADO. O TEXTTO É INSERIDO NO INÍCIO DO ARQUIVO
# a             DE APPEND, ESCRITA PRESERVANDO O CONTÉÚDO EXSTENTE. ARQUIVO É CRIADO SENÃO EXISTIR,É INSERIDO NO FINAL DO ARQUIVO
# b             MODO BÍNARIO
# +             ATUALIZAÇÃO DE LEITURA E ESCRITA
# x             ABRE O ARQUIVO PARA CRIAÇÃO EXCLUSIVA. FALHANDO SE  O ARQUIVO EXISTIR.

# OBS: PODEMOS COMBINAR OS MODOS EX. r+, w+, w+b. O MODO PADRÃO CASO NÃO SEJA ESPECIFICADO
# OBS: O MAIS USADO É " R "

'''                    ABRINDO UM ARQUIVO: FUNÇÃO OPEN()'''
''' '''


