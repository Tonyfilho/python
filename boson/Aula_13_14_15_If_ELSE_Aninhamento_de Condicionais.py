'''ANINHAMENTO DE CONDICIONAIS'''

'''IF Condição ENTÂO:  Instruções de condição VERDADEIRA'''

'''ELSE IF Condição2 ENTÂO: Instruções de Condição2 VERDADEIRA '''

'''ELSE : Instruções de Condição2 FALSA'''

#exemplos abaixo, onde calcularemos a Média 7 aprovado, acima de 5 Recuperação e Abaixo de 5 Reprovado:
from time import sleep
n1 = float(input('Digite a Nota da 1º Prova: '))
n2 = float(input('Digite a Nota da 2ª Prova: '))
media = (n1 + n2) / 2
print('PROCESSANDO......TEM UM BURRO ME OLHANDO ....LOL')
sleep(1)
print('Sua Média É: {:.2f}' .format(media))
print('#*#' * 15)
if media >= 7: # ESTA É A 1º CONDIÇÃO
    resultado = 'Aprovado'
    print('Você foi {}, Parabéns!'.format(resultado))
else:
    if media >= 5:
        resultado = 'Recuperacao'
        print('Você está de {}, Terá que refazer a Matéria que não Passou.'.format(resultado))

    else:
        resultado = 'Reprovado'
        print('Você ficou {} seu Orelha! Volte a Estudar.'.format(resultado))
print('#*#' * 15)

sleep(2)
print('Mais Um Ano Findo.....')