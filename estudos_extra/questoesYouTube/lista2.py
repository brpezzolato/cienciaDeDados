faturamento = 45000
custo = 23500
lucro = faturamento - custo
margem = lucro / faturamento

print(f"Faturamento: R$ {lucro:,.2f} e a margem {margem:.0%}")

# ---------------------------------------------------------------------------------------------------------

nome = " mArcOs antonio rOcha "
email = " MARCOS.ROCHA@GMAIL.COM "

nome = nome.strip()  # Tira os espacos duplicados e errados
# nome = nome.capitalize() (Primeira letra maiuscula da frase)
nome = nome.title()  # Cada comeco de palavra em maiusculo
print(nome)

email = email.strip()
email = email.lower()  # Deixa em letra maiuscula

print(email)

# ---------------------------------------------------------------------------------------------------------

email = "andre.silva@empresa.com.br"
novoDominio = "@grupocorp.com"
posicaoArroba = email.find("@")

email = email[:11] + novoDominio

print(email)

# ---------------------------------------------------------------------------------------------------------

