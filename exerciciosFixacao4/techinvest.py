print("\nPrime o simulador de investimentos da TechInvest\n")

nome = str(input("Envie o seu nome: "))
renda = float(input("Envie o valor da sua renda mensal: "))
gastoMensal = float(input("Envie o valor do seu gasto mensal: "))

while True:
    nivelCoragem = int(input("Envie o seu nível de coragem (1 a 10): "))
    if nivelCoragem < 1 or nivelCoragem > 10:
        print("Digite um valor entre 1 e 10")
    else:
        break

reserva = gastoMensal * 6
qntFalta = reserva - (renda - gastoMensal)

if gastoMensal <= renda:
    if qntFalta <= 0:
        print(f"\nVoce pode fazer tua reserva de emergencia para 6 meses de gasto (R$ {reserva:.2f}) e vai te sobrar ainda R$ {qntFalta * -1:.2f}\n")
    else:
        print(f"\nPra sua reserva de 6 meses de gasto (R$ {reserva:.2f}) ainda falta R$ {qntFalta:.2f}\n")
else:
    print("\nEmergencia financeira\n")

if nivelCoragem < 4:
    ondeInvestir = "Tesouro direto"
    calculo = 1.15
elif nivelCoragem >= 4 and nivelCoragem <= 7:
    ondeInvestir = "Fundo imobiliario"
    calculo = 1.21
else:
    ondeInvestir = "Acoes de tecnologia"
    calculo = 1.32

print(f"{nome} de acordo com o seu perfil voce quer assumir um risco {nivelCoragem} assim faremos a simulacao em {ondeInvestir}\n")

while True:
    maisAlgo = float(input("Voce tem algum valor a mais guardado que deseja adicionar na simulacao ? (0 pra nao): "))
    if maisAlgo < 0:
        print("Esse valor e invalido")
    else:
        break

qtsAnos = int(input("Quantos anos que voce pretende investir: "))

montante = (renda - gastoMensal) + maisAlgo
antigo = montante

print(
    f"Com o valor que sobrou da sua renda mensal apos os gastos, voce tem R$ {montante:.2f} nessa simulacao, e com base na sua coragem voce investira em {ondeInvestir} que rende {(calculo -1 )* 100:.0f}% ao ano\n"
)

for i in range(qtsAnos):
    montante *= calculo
    print(
        f"No ano {i + 1} de investimento em {ondeInvestir} de R$ {antigo:.2f} vai para R$ {montante:.2f} ({(calculo -1 )* 100:.0f}% no ano) ganho de R$ {montante - antigo:.2f}"
    )
    antigo = montante

print(f"\nEm {qtsAnos} anos em {ondeInvestir} voce vai ter um montante de R$ {montante:.2f} ganho de R$ {montante - (renda - gastoMensal):.2f}\n")