def soma2 (num01, num02):
    resp = num01 + num02
    return resp

resposta = soma2(1000, 500)
print(resposta, ' Na linha 7')

resposta = soma2(15.9, 11.1)
print(resposta,'linha 10')


def imprime ():
    print('oi')
imprime()

def tem_sete_itens (i):
    if len(i) == 7:
        return True
    else:
        return False

print(tem_sete_itens('ISTO AQUI TEM 7'),'na linha 22')
print(tem_sete_itens('1234567'),'na linha 23 temos 7 itens')

if tem_sete_itens('7itens7'):
    print('realmente temos 7 itens')
