#Extrair domínio de um e-mail

email= "lolla@gmail.com"
dominio = email[email.index("@")+1:] #pega tudo depois do arroba
print(dominio) #"gmail.com"

#Pegar dia, mês e ano de uma data

data = "11/12/2025"
dia = data[:2]  # primeiros 2 caracteres
mes = data [3:5]  # do índice 3 até 4
ano = data[6:]# do índice 6 até o fim
print(dia, mes, ano)

#Extrair primeiro nome

nome_completo = "Maria Cecilia Alves"
primeiro_nome = nome_completo.split()[0]  # divide por espaço e pega o primeiro
print (primeiro_nome) #Maria

#Inverter um texto

frase = "Querer sem ação é só delirio"
invertida = frase[::-1]
print(invertida) #oiriled ós é oãça mes rereuQ
