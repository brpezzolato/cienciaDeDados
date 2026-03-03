salario = float(input("Digite o valor do salario: R$ "))

if salario <= 280:
    aumento = 1.20
elif salario <= 700:
    aumento = 1.15
elif salario <= 1500:
    aumento = 1.10
else:
    aumento = 1.05

novoSalario = salario * aumento
valorAumento = novoSalario - salario
porcentagem = (aumento - 1) * 100

print(
    "\n"
    f"Salario antes do aumento: R$ {salario:.2f}\n"
    f"Percentual: {porcentagem:.0f}%\n"
    f"Valor do aumento: R$ {valorAumento:.2f}\n"
    f"Novo salario: R$ {novoSalario:.2f}"
)