renda = float(input("Envie o valor da sua renda mensal: "))
gastoMensal = float(input("Envie o valor do seu gasto mensal: "))

while True:
    nivelCoragem = int(input("Envie o seu nível de coragem (1 a 10): "))
    if nivelCoragem < 1 or nivelCoragem > 10:
        print('Digite um valor entre 1 e 10')
    else:
        break

reserva = gastoMensal * 6
qntFalta = reserva - (renda - gastoMensal)

if gastoMensal <= renda:
    print(f"\nPra sua reserva de R$ {reserva:.2f} 6 vzs o valor do seu gasto faltam {qntFalta <= 0 and f'Voce pode ja cobrir 100% da tua reserva' or f'R$  {qntFalta:.2f}'}\n")
else:
    print("\nEmergencia financeira\n")

if nivelCoragem < 4:
    ondeInvestir = "Tesouro direto"
elif nivelCoragem >= 4 and nivelCoragem <= 7:
    ondeInvestir = "Fundo imobiliario"
else:
    ondeInvestir = "Acoes de tecnologia"


print(ondeInvestir)
