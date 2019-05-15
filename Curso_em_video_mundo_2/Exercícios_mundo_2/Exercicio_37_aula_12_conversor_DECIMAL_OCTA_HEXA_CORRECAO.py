'''ESTA  É A CORREÇÃO DO EXERCÍCIO DE NUMERO 37 DA AULA 12, DE ACORDO COM O VIDEO 37'''

num = int(input('Digite um Numero Inteiro: '))
print('''Escolha uma das BASES de CALCULOS:
[ 0 ] Converter para BÍNARIO
[ 1 ] Converter para OCTAL
[ 2 ] Converter para HEXADECIMAL''')
print('\033[1;36m *-*' * 15 + '\033[m')
opcao = int(input('Digite aqui sua OPÇÃO '))
print('\033[1;36m *-*' * 15 + '\033[m')
print(opcao)

#  INICIO DA CONDIÇÕES DE ESCOLHAS ANINHADA

if   opcao == 0:
    print('O Nº {}, convertido para BÍNARIO é igual a {}'.format(num, bin(num)[2:]))#  O [2:]FATIA A STRING, ELIMINADO OS 2º NUMEROS DE CONTROLE DO PYTHON
elif opcao == 1:
    print('O Nº {}, convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
#  O [2:]FATIA A STRING, ELIMINADO OS 2º NUMEROS DE CONTROLE DO PYTHON
elif opcao == 2:
    print('O Nº {}, convertido para HEXADECIMAL é igual a {}'.format(num, bin(num)[2:]))
#  O [2:]FATIA A STRING, ELIMINADO OS 2º NUMEROS DE CONTROLE DO PYTHON
else:
    print('OPÇÃO INVÁLIDA, FV COMEÇE NOVAMENTE')