'''NESTE  AULA ESTAREMOS DANDO EXEMPLO DE USO DE 2 MODULOS AO MESMO TEMPO'''

'''USAREMOS O RANDOM.RANDINT PARA GERAR UM NUMERO ALEATÓRIO PARA NOSSO OUTRO MODULO'''

from Exercicio_31_MODULO_modulacoes import * # DESTA FORMA (*) PODEMOS IMPORTAR SEM PRECISA ESCREVER O NOME DO MÓDULO
# Estamos dizendo que queremos TODOS (*)
import random

mensagens()

numero_aleatorio = random.randint(1, 20) # AQUI CRIAMOS A VAR COM NUMERO ALEATÓRIO

print(numero_aleatorio)

retorno_fatorial = fatorial(numero_aleatorio)

print(retorno_fatorial)


retorno_fibonacci = fibonacci(numero_aleatorio)

print(retorno_fibonacci)
