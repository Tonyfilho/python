'''Aula_09_Modulo_Rondom.py'''

'''Modulo Random faz geração de numeros e outros de forma ALEATÓRIA'''
import  random, math

#temos 2s principais funcões:

# RANDOM.RANDOM() que gera numeros aleatório de 0 a 1
print(random.random()) # aqui imprimiremos de 0 a 1
print('*-*' * 30)
n1 = float(10) *random.random() #Aqui imprimiremos de 0 a 10
n2 = float(100) *random.random()#Aqui imprimiremos de 0 a 100 aleatoriamente
n3 = float(1000) *random.random()#Aqui imprimiremos de 0 a 1000
n4 = random.randint(0, 1000)  # é a mesma coisa que o de cima.
print(f'{n1}')
print('*-*' * 30)
print('{}'.format(n2))
print('*-*' * 30)
print('{:.0f}'.format(n3)) #com ZERO de casa decimal {:.0f}
print('*-*' * 30)
print(math.ceil(n3)) # aqui usamos o MATH.CEIL para aredondar para numero é o mesmo que {:.0f}
print('*-*' * 30)
print(f'{n4}')






