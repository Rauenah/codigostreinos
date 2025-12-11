#CONTROLE DE REPETIÇÃO
#DENTRO DOS LOOPS, VOCÊ PODE CONTROLAR O FLUXO:
#BREAK >> INTERROMPE O LOOP ANTES DO FIM
#CONTINUE >> PULA PARA PRÓXIMA INTERAÇÃO

for numero in range(10):
    if numero == 5:
        break #para o loop quando chega em 5
    if numero % 2 == 0:
        continue #pula os numeros pares
    print(numero)

# A FUNÇÃO RANGE() SERVE PARA GERAR UMA SEQUENCIA DE NUMEROS

#SINTASE BASICA RANGE(INICIO, FIM, PASSO) START, AND, STEP

#inicio → número inicial da sequência (opcional, padrão é 0).
#fim → número final (não é incluído na sequência).
#passo → de quanto em quanto a sequência avança (opcional, padrão é 1).