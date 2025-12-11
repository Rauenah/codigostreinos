#Exemplo simulando como uma empresa poderia usar fatiamento string para marcar
#transações suspeitas automaticamente:


#BIN (primeiros 6 dígitos) → usado para identificar bancos emissores suspeitos.
#Últimos 4 dígitos → exibidos em relatórios sem expor o cartão inteiro.
#Domínio do e-mail → detecta cadastros com provedores descartáveis.
#Valor da transação → regra simples para marcar valores muito altos.



# Lista de transações simuladas
transacoes = [
    {"cartao": "4532123456789012", "valor": 500, "email": "cliente@tempmail.com"},
    {"cartao": "6011123456789999", "valor": 50,  "email": "user@gmail.com"},
    {"cartao": "4532129876543210", "valor": 2000, "email": "fraude@tempmail.com"},
]

# Lista de BINs (primeiros 6 dígitos) considerados de alto risco
bins_suspeitos = ["453212"]

# Lista de domínios de e-mail suspeitos
dominios_suspeitos = ["tempmail.com", "mailinator.com"]

# Função para verificar suspeitas
def verificar_fraude(transacao):
    cartao = transacao["cartao"]
    email = transacao["email"]

    # Extrair BIN (primeiros 6 dígitos)
    bin = cartao[:6]

    # Extrair últimos 4 dígitos (para relatórios)
    ultimos = cartao[-4:]

    # Extrair domínio do e-mail
    dominio = email[email.index("@")+1:]

    # Regras simples de fraude
    if bin in bins_suspeitos or dominio in dominios_suspeitos or transacao["valor"] > 1000:
        print(f"⚠️ Transação suspeita! Cartão ****{ultimos}, valor R${transacao['valor']}, domínio {dominio}")
    else:
        print(f"✅ Transação aprovada. Cartão ****{ultimos}, valor R${transacao['valor']}")

# Testando
for t in transacoes:
    verificar_fraude(t)