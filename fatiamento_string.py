#Fatiamento de string em Python é a técnica de pegar partes #específicas de uma string usando índices.
#Como as strings são sequências, você pode acessar intervalos 
# #decaracteres com a sintaxe:

##string[inicio:fim:passo]

#início → posição inicial (inclusiva)
#fim → posição final (exclusiva)
#passo → intervalo entre os caracteres (opcional)

texto = "Python"

# Pegar do índice 0 até o 2 (não inclui o 3)
print(texto[0:3])   # "Pyt"

# Omitindo início → começa do começo
print(texto[:4])    # "Pyth"

# Omitindo fim → vai até o final
print(texto[2:])    # "thon"

# Usando passo → pula caracteres
print(texto[::2])   # "Pto"  (pega de 2 em 2)

# Índices negativos → contam de trás para frente
print(texto[-3:])   # "hon"

# Invertendo a string com passo -1
print(texto[::-1])  # "nohtyP"


#Resumindo
#Fatiamento é como “cortar” a string em pedaços.
#Usa a notação .
#É muito útil para manipulação de texto, como extrair palavras, inverter ou selecionar partes específicas.


