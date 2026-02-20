saldo_inicial = 1000.0
checkpoint = saldo_inicial
carac = "!@#$%^&*()"

print(saldo_inicial is checkpoint)

while True:
    nome = input("\nDigite seu nome: ")
    status = False

    for i in carac:
        if i in nome:
            status = True

    if status == True:
        print("\nNome invalido, caracterie especial e proibido\n")
    else:
        break

for i in range(4):
    num = float(input(f"Digite um valor e realize opeacoes {i + 1}: "))

    if num > 0:
        saldo_inicial += num
        print(f"Saldo parcial: {saldo_inicial}\n")

    elif num < 0:
        if num * -1 > saldo_inicial:
            print("Saldo insuficiente\n")
        else:
            saldo_inicial += num
            print(f"Saldo parcial: {saldo_inicial}\n")


print(f"\nO seu saldo final e: {saldo_inicial}")
print(f"\nE igual a check point ? {saldo_inicial is checkpoint}")