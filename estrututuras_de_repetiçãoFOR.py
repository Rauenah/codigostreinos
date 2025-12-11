#Em Python, ESTRUTUTAS DE REPETIÇÃO(também chamadas de loops)
#são comandos que permitem executar um bloco de código varias vezes
#de forma automatica, sem precisar escrever o mesmo trecho repetidamente

#FOR USADO QUANDO VOCÊ SABE QUANTAS VEZES QUER REPETIR OU QUANDO PERCORRE
#UMA SEQUENCIA(LISTA, STRING, RANGE)

texto = input ("Informe um texto ")
VOGAIS ="AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
        
else:   
    print()  #adc uma quebra de linha  
    print("Execute no final da linha ")       

#Lê um texto do usuário.
#Percorre cada letra.
#Verifica se é vogal (independente de maiúscula ou minúscula).
#Imprime só as vogais, todas juntas.
