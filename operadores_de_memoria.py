#Os operadores de identidade em Python são usados para verificar se duas variaveis apontam para o mesmo
#objeto na memoria, não apenas se os valores são iguais.
# Eles sempre retornam o valor booleano TRUE ou FALSE

#IS Retorna True se duas variáveis são o mesmo objeto (mesmo endereço na memória).

a = [1,2,3]
b = print (a is b) #True (b aponta para o mesmo objeto que a)

#IS NOT Retorna  se duas variáveis não são o mesmo objeto.

a = [1,2,3]
b = [1,2,2]
print(a is not b) # True (mesmo conteúdo, mas objetos diferentes na memória)

#Diferença entre identidade e igualdade

	#Igualdade (==) → compara os valores.
	#Identidade (is) → compara se são o mesmo objeto.
