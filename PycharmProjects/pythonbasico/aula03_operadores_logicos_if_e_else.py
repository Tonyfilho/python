# Comparações: =="IQUAL" !="DIFERENTE"   >"MAIOR"  <"MENOR"
# >="MAIOR OU IGUAL"  <="MENOR OU IGUAL"
# AND e OR e ELSE "SENÂO"

# Exemplo:

a = 2
b = 1
c = 20

if a > b: #ou seja se A for maior que B vamos imrimir
    print(a, 'Somente se for maior que:', b)

'''vimos no resultado abaixo que foi impresso'''

if a > c: # ou seja se A for maior que C, mas C é 20
    print(a, 'Somente se for maior que 20:', c)
'''vimos que NÂO foi impresso a 2ª linha de comando'''

# para resolvermos isto usamos o ELSE "então" onde ele responde
# fazendo a resposta ou retorno do resultado, veja a baixo:

if a > c:
    print(a,'Somente se for maior que 20 ou C:', c)
else: #Ou Seja com ELSE,fizemos uma comparação e o programa descidiu
    print(a, 'não é maior do que:', c)







