'''   EXPRESSÕES E O PERADORES ARITMÉTICOS'''

# + = soma
# - = subtração
# * = multiplicação
# / = divisão
# ** = expodenciação ou potenciação .

a = 5
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b) #ou seja 5 elevado a 4 ou 5x5x5x5
print(a * a * a * a ) # ou (a ** b)

#Podemos armazenar  os valores em uma variável veja:
c = a ** b
print( c , 'Este é o valor de "C"' )

# Vamos criar expressões mais complexas:

d = a + a * b
print( d , 'Este é o valor de "D" nesta ordem aritmetica : a + ( a * b )')

d = (a + a) * b
print( d , 'Este é o valor de "D" nesta ordem aritmetica : (a + a) * b')
'''São feitas nestas ordens:
1º expodenciação
2º multiplicação e divisão
3º soma e subtração
NO 1º Exemplo ele MULTIPLICOU A * B e + A deu 25
no 2º Exemplo por causa do PARENTES e 
SOMOU A+A e MULTIPLICOU POR B: A + A * B deu 40, 
desta forma temos que usar os PARENTES para mudar ordem.
'''
# exemplo de equação de 2º Grau:
# x2 + 2x + 3 = 0
# A    B    C
# queremos calcular  o DELTA da equação: b2 - 4ac
# ou seja A vale 1, B vale 2 e C vale 3.
a = 1
b = 2
c = 3
#escreveremos  uma expressão que calcule a equação de 2º grau
#vamos ARMAZERAR o resultado em uma variável 'DELTA'
delta = b ** b - 4 * a * c  # ou seja isto 'b2 - 4ac'
print( delta, ' Este é o valor de Delta')













