from random import choice

n = [2, 5, 9, 1, 4]
res = choice(n) % n[0]
print(res)

texto = 'Tres Pratos de Trigo para Tigres Tristes'
total = texto.upper().count(texto[0])
print(total)

from random import randint
num = randint(1, 6)
res = num // 2
print(res)