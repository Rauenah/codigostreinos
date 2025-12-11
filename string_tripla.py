#Uma string tripla em Python é uma string delimitada por três aspas-
#pode ser "texto" ou """texto"""

#Permite escrever texto em múltiplas linhas sem precisar usar .
#Muito usada para docstrings (documentação de funções, classes e módulos).
#Pode conter aspas simples ou duplas dentro dela sem precisar escapar.

#Em resumo: strings triplas são ideais para textos longos, 
# multilinhas ou documentação.

#String em múltiplas linhas

mensagem = """Essa mensagem é uma string que ocupa varias linhas sem precisar usar \\n."""
print(mensagem)

#Docstring em função

def soma(a,b):
    """Essa função recebe dois números e retorna a soma deles"""
    return a+ b   #Aqui, a string tripla serve como documentação da função.

#Contendo aspas sem escapar

texto = '''Ele disse: "Python é incrivel"'''
print(texto)

#Em resumo: strings triplas são ideais para textos longos, multilinhas ou documentação.
