#DEFINIÇÃO DE CONSTANTES

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

#INFORMAÇÃO DA CONTA

saldo = 2000
cheque_especial = 450
tipo_de_conta = "normal", "universitaria"

#PERGUNTE AO USUARIO QUE TIPO DE CONTA

tipo_de_conta = input("Digite o tipo de conta(normal/universitaria):").lower

#PERGUNTE O VALOR DO SAQUE

saque = int(input("Digite o valor do saque: "))

#LOGICA DO SAQUE

if  tipo_de_conta == "normal":
    if saldo >= saque:
        print("Saque realizado com sucesso ")
    elif saque <= (saldo + cheque_especial):
         print("Saque realizado com uso do cheque especial")
    else:
        print("Não foi possivel realizar saque, saldo insuficiente")

elif tipo_de_conta == "universitaria":
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente! ")

else:
    print("Sistema não reconhece esse tipo de conta, entre em contato com seu gerente.")


     #voltar nesse codigo 10/12/2025