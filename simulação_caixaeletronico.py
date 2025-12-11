#SIMULAÇÃO CAIXA ELETRÔNICO

saldo = 2000
cheque_especial = 500

while True:
  print("\n===Caixa eletrônico===")
  print("1-Consultar saldo")
  print("2-Sacar dinheiro")
  print("3-Depósito dinheiro")
  print("0-Sair")

  opção = input("Escolha uma opção: ")

  if opção =="1":
    print(f"Seu saldo atual é: R$ {saldo}")

  elif opção == "2":
    valor =float(input("Digite o valor do saque:"))
    if valor <= saldo + cheque_especial:
       saldo -= valor
       print(f"Saque  de R${valor} realizado com sucesso! ")
       print(f"Saldo atual: R$ {saldo}")
    else:
        print("Saldo insuficiente") 

  elif opção == "3":
       valor =float(input("Digite o valor do depósito:")) 
       saldo += valor
       print(f"Depósito de R${valor} realizado com sucesso!") 
       print(f"Saldo atual:R$ {saldo}")  
    
  elif opção == "0":
     print("Encerrando o sistema...Obrigado por usar nosso caixa eletrôno!")
     break #encerra o loop
  
  else:
     print("Opção inválida!Tente novamente.")

        
     
    