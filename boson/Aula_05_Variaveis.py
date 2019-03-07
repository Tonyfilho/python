''' conseito de variaveis em PYTHON: A VIAAVEL É UMA POSIÇÃO
NA MEMORIA que é dividida e é dado um nome

as variaveis são endereçadas em formato hexadecimal

e as variaveis tem um TIPO que determinado tipo

1 variavel permite por 1 informação por vez em caso de varias
temos que usar as LISTAS e as AREAYS

Imagine a memoria ram como se fosse um grade com varios numeros e de endereço

no nosso casa damos um ROTULO ou um NOME desta for o programa sabe qual
parte da memoria se encontra a informação

os tIPO são classificados em 3 grades categoria:

1-0 NUMERICOS
NUMEROS INTEIROS EX.1, 3 OU 98
NUMEROS DE PONTO FLUTUANTE EX. 1.4, 89.7 (ESTE SAPARADOS POR PONTO)

2-0  LÓGICOS
BOOLEANOS EX. VERDADEIRO OU FALSO

3-0 OS LITERAIS (QUALQUER CARACTERES)
CARACTERES E STRING DE CARACTERES EX. 'EU SOU UM STRING'

'''

## SEMPRE antes fazer , precisa DECLARAR  antes de usar, e as variaveis devem ter VALOR ou inicializaveis ou
# seja por uma informação ex.

nome = 'tony'  ## lembre para por um conj. de caracteres precisa por as 'ASPAS'
convidado = True
numero = 5.0
numero2 = 60


''' Função TYPE retorna o tipo da variavel vejamos os exemplos'''

print(type(nome))  # Olhe que imprimiu <class 'str'> tipo STRING
print(type(convidado)) # Olhe que imprimiu <class 'bool'> tipo BOOLEANO
print(type(numero)) # Olhe que imprimiu <class 'float'> tipo FLUTUANTE
print(type(numero2)) # Olhe que imprimiu <class 'int'> tipo INTEIRO

'''OBS.: Veja que não preciamos DECLARAR o TIPO  de variavel, o PYTHON já faz ito'''