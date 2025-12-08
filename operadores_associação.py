#Eles são usados para verificar se um valor está presente (ou não) dentro de uma sequência, 
#como listas, strings, tuplas ou dicionários.
#o resultado é sempre booleano TRUE ou FALSE

#IN Retorna TRUE se o valor existe dentro da sequencia

lista = [1,2,3,4]
print (2 in lista) #true
print(5 in lista)  #false


#NOT IN Retorna TRUE se o valor não existe dentro da sequência.

lista = [1,2,3,4]
print(5 not in lista)   # True
print(2 not in lista)   # False

texto = "Python"
print("Java" not in texto)  # True

#EXEMPLO VERIFICAR SE ITEM ESTÁ NA LISTA:

frutas = ["maça", "laranja", "kiwi"]
if "banana" in frutas:
    print("Tem banana na lista")


#VERIFICAR SE CARACTERE ESTÁ EM UMA STRING

senha = "abc123"
if "@" not in senha:
    print("Senha precisa ter um caractere especial")
