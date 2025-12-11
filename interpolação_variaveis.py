#Interpolação de variáveis em Python é a técnica de inserir valores dentro de uma 
# #string de forma dinâmica, sem precisar concatenar manualmente. 
# Isso torna o código mais legível e prático.


# F-strings → mais moderno e legível.
# .format() → intermediário.
# % → legado, mas ainda funciona.

#1. F-strings (Python 3.6+)
#A forma mais moderna e recomendada:

nome = "lolla"
idade = 18
print(f"Meu nome é {nome} e tenho {idade} anos ") #saida: meu nome é lolla tenho 18 anos.
#As variáveis são colocadas entre {} dentro da string.
#Você pode até usar expressões:

print(f"Daqui 5 anos terei {idade + 5} anos")

#2. Método .format() mais antigo, mas ainda usado:

nome = "lolla"
idade = 25
print("Meu nome é {} e tenho {} anos.".format(nome, idade))

#também permite indices
print ("Meu nome é {0} e tenho {1} anos. {0} gosta de Python".format(nome, idade))

#3. Operador % (estilo C) Forma mais antiga, pouco usada hoje:

nome = "lolla"
idade= 25
print("Meu nome é %s e tenho %d anos." %(nome, idade))

# %s → string
#%d → número inteiro
#%f → número decimal















