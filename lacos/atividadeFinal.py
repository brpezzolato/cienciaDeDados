status = False
total = 0
count = 0
media = 0

while status == False:
    preco = float(input("Digite o preco do produto ao finalixar digite (0): "))

    if preco != 0 and preco > 0:
        count += 1
        total += preco

    elif preco < 0:
        print("\nPreco invalido digite novamente")
        preco = float(input("Digite o preco do produto ao finalixar digite (0): "))

    else:
        if count == 0 and preco == 0:
            status = True
        media = total / count
        formaPgto = int(input("(1 - Dinheiro / 2 - Cartão): "))
        if formaPgto == 1:
            total = total * 0.95
        print(
            f"\nTotal: {total}\nQtd de produtos: {count}\nMedia: {media}\nPagamento: {formaPgto}"
        )
        status = True
