
import modulo_aula06
#Passamos a importar nossas variaveis do nosso arquivo MODULO_AULA06,
# com isto n precisamos mais termos todas as variaveis declaradas.



'''TUPLA'''
'''Caso queiramos mudar um objeto da TUPLA não podemos
somente usar a forma comum usando  o EX.:  
'''
# minha_tupla_e = 'João' desta forma teremos erro. Pois temos
# que substituir o conteudo da TUPLA EX.:
minha_tupla_e = (('JUAN','MUTIZ') + modulo_aula06.minha_tupla_e )
print(minha_tupla_e)
'''
('JUAN', 'MUTIZ') aqui substituimos o valor por completo
ou TODOS os elementos dentro dela
A TUPLA normalmente é usado para OBJETOS ESTATIDOS onde 
não iremos ter ALTERAÇÕES no objeto.
'''
print(len(minha_tupla_e)) #Usando o LENS podemos decobrir
# o tamanho da tupla


