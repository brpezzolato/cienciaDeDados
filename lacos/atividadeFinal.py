status = False
total = 0
count = 0
media = 0

while status == False:
    preco = float(input("Digite o preco do produto para finalizar digite 0: "))

    if count == 0 and preco == 0:
        status = True
        print("\nOperacao finalizada")

    elif preco < 0:
        print("\nPreco invalido tente novamente")

    elif preco > 0:
        count += 1
        total += preco

    else:
        media = total / count
        formaPgto = int(input("(1 - Dinheiro / 2 - Cartão): "))
        if formaPgto == 1:
            total = total * 0.95
        print(
            f"\nTotal: {total}\nQtd de produtos: {count}\nMedia: {media:.2f}\nPagamento: {formaPgto:.2f}\n\nOperacao finalizada"
        )
        status = True
