#Exemplo de e-mail automático

nome = "Cecilia"
valor = 250.50
data = "11/12/2025"

mensagem= f"""
Olá {nome},

 Este é um aviso automático sobre sua última transação.

 Detalhes:
-Valor: R${valor}
-Data: {data}

Se você não reconhece esperação, entre em contato com nosso suporte

Atenciosamente,
Equipe de Segurança
"""

print(mensagem)


#Permitem escrever textos longos e organizados sem precisar concatenar.
#São ideais para mensagens multilinhas como relatórios, e-mails, contratos ou documentação.
#Combinadas com f-strings, ficam dinâmicas e personalizadas.
