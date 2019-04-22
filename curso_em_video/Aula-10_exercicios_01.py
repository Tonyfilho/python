'''exercicio simples com IF'''
'''Vemos neste exercicio que a variável tiver o nome TONY , ele entra em uma bloco
bloco do IF'''
nome = str(input('Digite seu nome: ')) .strip().upper()
if nome == 'TONY':
    print('Seu nome é Legal: {}'.format(nome))
else:
    print('Seu nome é comum !{}'.format(nome))
print('Bom dia, seja bem vindo {}'.format(nome))
print('***Fim***')