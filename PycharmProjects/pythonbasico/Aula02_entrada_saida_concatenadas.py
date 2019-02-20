nome = 'Tony'
idade = 45
altura = 1.90
# agora aprenderemos como CONCATENAR as coisa, ou seja JUNTA-LAS na mesma  linha de comando
# podemos usar o "," ou o "+" dentro da  função, veremos abaixo

print(nome, 'Tem',  idade,  'De Idade', 'E tem', altura, 'Metro de altura' )

# Podemos usar o "+" mas o mais usado é a VIRGULA, pois o "+" não gera o ESPAÇO entre os elementos, este ESPAÇO tem que se posto.

print(nome + 'Tem'+  idade +  'De Idade' + 'E tem' + altura + 'Metro de altura' )

# Quando usamos o "+" para contatena ALÉM do ERRO que deu, o PYTHON não converte INTEIROS em STRINGS por isto que usamos mais a ","
# podemos OBSERVAR que nas IDE marcou nossas VERIÀVEIS de MARROM.

# acertaremos os COD usando a FUNÇÃO "STR" onde a mesma converte a VARIÁVEL INTEIRA em STRING, lembrando que somente funciona em FLOAT E INTv.
print(nome + 'Tem'+ str(idade) + 'De Idade' + 'E tem' + str(altura) + 'Metro de altura' )

