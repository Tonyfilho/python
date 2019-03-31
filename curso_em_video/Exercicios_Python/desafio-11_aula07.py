'''fala um programa que MEÇA OU CALCULE A ÁREA DE UMA PAREDE, e a
quantidade necessária para pinta-la, sabendo que: Cada litro de  tinta
pinta m2 de parede'''
altura = float(input('Digite a Altura da Parede em metros: '))
comprimento = float(input('Digite o Comprimento da parade em metros: '))
metro_quadrados = altura * comprimento
tinta = metro_quadrados * 1

print(f'Quantidade Tinta é:{tinta}', 'Litros para pintar a Parade')



