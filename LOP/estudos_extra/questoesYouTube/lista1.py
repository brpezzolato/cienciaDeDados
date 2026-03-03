faturamento = 50000
bonus = 10

calculo = faturamento * ((100 - bonus) / 100)

print(f'Faturamento apos o desconto do Bonus: R$ {calculo} (Bonus de R$ {faturamento - calculo})')

# --------------------------------------------------------------------------------------------------------

inicio = 250

inicio -= 78
inicio += 100

print(f'Estoque do dia atualizado: {inicio}')

# ---------------------------------------------------------------------------------------------------------

qtsCaixas = 1250
capacidadeCaminhao = 12

calculoCaminhao = qtsCaixas // capacidadeCaminhao

calculoSobra = qtsCaixas % capacidadeCaminhao

print(f'Serao necessarios {calculoCaminhao} caminhoes e sobraram {calculoSobra} caixas para enviar em uma viagem menor')

# ---------------------------------------------------------------------------------------------------------

faturamento = 15000
custoFixo = 5000
imposto = 0.15

imposto = faturamento * imposto
lucroLiquido = faturamento - custoFixo - imposto
margem = lucroLiquido / faturamento

print(f'Faturamento: {faturamento}')
print(f'Lucro: {lucroLiquido}')
print(f'Margem: {margem}')

meta = margem > 0.3
print(f'Meta atingida ? {meta}')

# ---------------------------------------------------------------------------------------------------------

tempoTotal = 40

anos = tempoTotal // 12
meses = tempoTotal % 12

print(f'O contrato é de {anos} anos e {meses} meses')