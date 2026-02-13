salario = float(input("Insira o salario inicial: "))
percentual = 0.015
ano = 1995

while ano < 2024:
    salario = salario * (1 + percentual)
    print(f"{ano} ({percentual * 100}%) = R$ {salario:.2e}")
    percentual = percentual * 2
    ano += 1

print(f"\nSalario final ({ano}): R$ {salario:.2f}")
