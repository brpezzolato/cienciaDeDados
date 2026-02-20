saldo_inicial = 1000.0
checkpoint = saldo_inicial

print(saldo_inicial is checkpoint)

carac = "!@#$%^&*()"
countVeri = 0

while True:
    nome = input("Digite seu nome: ")
    status = False

    for i in carac:
        if i in nome:
            status = True

    if status == True:
        print("Nome invalido nao pode caracterie especial")
    else:
        break

for i in range(4):
    num = float(input(f"Digite um valor e realize opeacoes {i + 1}: "))

    if num > 0:
        saldo_inicial += num
        num > 500 and print('Valor alto')
        print(f"Saldo parcial: {saldo_inicial}")

    elif num < 0:
        if num * -1 > saldo_inicial:
            print("Saldo insuficiente")
        else:
            saldo_inicial += num
            print(f"Saldo parcial: {saldo_inicial}")
            num < -500 and print('Valor alto')


print(f"\nO seu saldo final e: {saldo_inicial}")
print(f"E igual a check point: {saldo_inicial is checkpoint}\n")