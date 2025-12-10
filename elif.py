MAIOR_IDADE =18
IDADE_ESPECIAL = 17

idade = int(input("Digite sua idade: "))

if idade >= MAIOR_IDADE:
   print("Maior de idade, pode tirar CNH") 
elif idade == IDADE_ESPECIAL:
     print("Pode fazer aulas teoricas, mas não pode fazer aulas práticas")              
else:
     print("Ainda não pode tirar CNH")


     #elif condições alternativas

#if → testa a primeira condição.
#elif → testa uma condição alternativa, caso o if seja falso.
#else → executa se nenhuma das condições anteriores for verdadeira.