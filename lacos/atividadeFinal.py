status = False
total = 0
count = 0
media = 0

while status == False:
    preco = float(input("Digite o preco do produto para finalizar digite 0: "))

    if count == 0 and preco == 0:
        status = True
        print("\nOperacao finalizada")

    elif preco > 0:
        count += 1
        total += preco

    elif preco < 0:
        print("\nPreco invalido digite novamente")
        preco = float(input("Digite o preco do produto ao finalixar digite (0): "))

    else:
        media = total / count
        formaPgto = int(input("(1 - Dinheiro / 2 - Cartão): "))
        if formaPgto == 1:
            total = total * 0.95
        print(
            f"\nTotal: {total}\nQtd de produtos: {count}\nMedia: {media}\nPagamento: {formaPgto}\n\nOperacao finalizada"
        )
        status = True
