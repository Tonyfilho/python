'''Faça um exercicio
faço um programa que leia do usuario 5 nome
usando o INPUT, usando 1 linha com while ou for

ou faça um programa que leia uma quantidade de pessoa para uma festa, apos isto
o programa irá ler a quantidade de pessoas, e depois  imprima
usaremos: o programa irá perguntar o nome de todas pessoa e por em uma lista de convidados
list,
entrada e saida
for in
while
'''

print('Este  é o Programa de cadastro de Convidados, Favor insira seus dados:')
print('######################################################################\n')
numero_de_convidados = input('Digite o Numero de Convidados : ')
lista_de_convidados = [] # criamos uma lista para adciona-la com as informações
# da variavel NOME_DO_CONVIDADO
i = 1
while i <= int(numero_de_convidados):
    nome_do_convidado = input('Digite o nome dos Convidados' ' Nº ' + str(i)+  ' Bem vindos:')
    lista_de_convidados.append(nome_do_convidado)# A lista está vazia
    # assim colocamos algum item na VARIAVEL nome_do_convidado nós
    # o PARAMETRO .APPEND (adciona) informações na lista

    i += 1
for convidado in lista_de_convidados:
    print(convidado) # Aqui com FOR IN conseguimos imprimir por ordem
    # a lista de convidados, Pois ele pega as informações em LISTA_DE_CONVIDADOS
    # e coloca na variavel CONVIDADO e imprimos.





