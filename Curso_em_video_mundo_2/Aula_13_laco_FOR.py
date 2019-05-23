''' ESTAREMOS ESTUDANDO O LAÇO FOR RANGE'''

# FOR I IN RANGE(0, 10) , Sendo que I, é uma variável que  pode ter qualquer nome.

lista = (1, 2, 3, 4)
for i in lista:
    x2 = (i ** 2 )
    print(x2)

'''                          exemplo do laço FOR simples com RANGE'''
estring = 'Oi'
for i in range(0, 15): # se usar o RANGE, preciso usar o contador??
#   contador = (i * 10) # se usar o contador não uso o range?
    print(estring)
print('fim'.upper())

'''                      EXEMPLO de laço FOR RANGE contato do maior para  o menor'''
for i in range(100, 0, -5): # CONTAGEM REGRESSIVA DE 5 A 5, começando por 100
    print(i)
print('fim'.upper())

'''                      EXEMPLO de laço FOR e RANGE com variável de INPUT dentro do RANGER'''
n = int(input('digite um numero: '.upper()))
for i in range(0, n):# ele vai contar de 0 ao NUMERO DIGITADO -1
    print(i)
print('fim'.upper())

'''                    EXEMPLO  de laço FOR e  RANGE com variáveis dentro do RANGE, mudando as configurações'''
i = int(input('digite inicio do range: '.upper()))
f = int(input('digite o fim do range: '.upper()))
p = int(input('digite o passo do range: '.upper()))
for i in range(i, f+1, p): # o F  é o RANGE + 1 ,com isto mudamos as conf. do range
    print(i)
print('fim'.upper())

# estou há 24 m do video



'''                            exemplo com FOR e IF Aninhados'''

