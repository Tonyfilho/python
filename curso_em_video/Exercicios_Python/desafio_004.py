'''Fazer um script usando,usando o métado de teste  .IS '''
'''OBS: Sempre o INPUT é sempre será STRING, mas metado de teste, mostra 
se podemos converte-lo  em algo '''
'''Todo OBJETO tem CARACTERISCA execultam funções e 
tudo que estiver dentro do "(PARENTESES)" são OBJETO, e todo OBJETO tem METADOS'''

o_que_e = input('Digite algo: ')
print('é numero ou letra?:{}',  o_que_e.isalnum(), type(o_que_e).format(o_que_e))  # é numero?
print('é Alfha numerico ?:{}', o_que_e.isalpha(), type(o_que_e).format(o_que_e))  # é Alfha numerico ?
print('é decimal?:{}', o_que_e.isdecimal(), type(o_que_e).format(o_que_e))  # é decimal?
print('é digito?:{}', o_que_e.isdigit(), type(o_que_e).format(o_que_e))  # é digito?
print('é indentificado?:{}', o_que_e.isidentifier(), type(o_que_e).format(o_que_e))  # é indentificado ?
print('é caixa baixa?:{}', o_que_e.islower(), type(o_que_e).format(o_que_e))  # é caixa baixa?
print('é caixa alta?:{}', o_que_e.isupper(), type(o_que_e).format(o_que_e))  # é caixa alta?

