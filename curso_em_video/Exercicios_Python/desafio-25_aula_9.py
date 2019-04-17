'''crie  um programa que  leia o nome de uma pessoa e diga se ela tem o SILVA no nome

usando como resporta TRUE or FALSE '''

nome = str(input('Digite seu nome: ')).strip().upper()
print(nome.find('SILVA'))

print('Temos o nome Silva Digitado?: ', 'SILVA' in nome)

print('Temos o nome Silva Digitado?: ', f'SILVA' in nome)


print('Seu nome tem Silva?: {}'.format('SILVA' in  nome))

print('Temos o nome Silva Digitado?: {}'.format(nome.upper()[:] == "SILVA"))  # neste metado não funciona com mais de 1 nome