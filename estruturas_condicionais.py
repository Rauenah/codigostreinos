MAIOR_IDADE= 18

idade=int(input("Informe sua idade: "))

if idade >= 18:
   print("Maior de idade, pode tirar CNH ")

if idade <  MAIOR_IDADE:
   print("Ainda não pode tirar CNH")

#SIMPLIFICANDO O CODIGO USANDO ELSE

MAIOR_IDADE = 18

idade= int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
   print("Maior de idade, pode tirar CNH")
else:
   print("Ainda não pode tirar CNH") 

#USANDO ELIF

MAIOR_IDADE =18
IDADE_ESPECIAL = 17

idade = int(input("Digite sua idade: "))

if idade >= MAIOR_IDADE:
   print("Maior de idade, pode tirar CNH") 
elif idade == IDADE_ESPECIAL:
     print("Pode fazer aulas teoricas, mas não pode fazer aulas práticas")              
else:
     print("Ainda não pode tirar CNH")
