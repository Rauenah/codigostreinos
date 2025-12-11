#Em Python, a classe de strings é representada pelo tipo embutido  
#usado para manipular textos. 
#Strings são imutáveis, ou seja, não podem ser alteradas depois de criadas; qualquer #modificação gera uma nova string

#len(s) → retorna o tamanho da string. 
# str(x) → converte valores em string.
#Métodos como .upper(), .lower(), .strip(), .replace(), .split() facilitam manipulação.

#upper() → deixa tudo em maiúsculo
#lower() → deixa tudo em minúsculo
#strip() → tira espaços extras das pontas
#replace(a, b) → troca a por b
#split() → quebra a string em partes (lista)

# String de exemplo
texto = "  Olá Mundo  "

# .upper() → transforma tudo em maiúsculas
print(texto.upper())   # "  OLÁ MUNDO  "

# .lower() → transforma tudo em minúsculas
print(texto.lower())   # "  olá mundo  "

# .strip() → remove espaços extras do início e do fim
print(texto.strip())   # "Olá Mundo"

# .replace() → substitui partes da string
print(texto.replace("Mundo", "Python"))   # "  Olá Python  "

# .split() → divide a string em uma lista, usando espaço como separador
print(texto.split())   # ['Olá', 'Mundo']
