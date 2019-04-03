'''está  é a correção de acordo com o curso'''

from  math import radians, tan, sin, cos
angulo = float(input('Digite o Valor do ângulo: '))
cosseno = cos(radians(angulo))
seno = sin(radians(angulo))
tangente = tan(radians(angulo))
print(f'O valor do Ângulo Calculado É: {angulo:.0f}', f'\n O Seno do ângulo É: {seno:.0f}', f'\nO Cosseno do ângulo É: {cosseno:.2f}', f'\nA Tangente do ângulo É: {tangente:.0f}')

