status = False
total = 0
count = 0

while status == False:
    preco = float(input("Digite o preco do produto para finalizar digite 0: "))

    if count == 0 and preco == 0:
        status = True
        print("\nFinalizado")

    elif preco < 0:
        print("Preco invalido tente novamente\n")

    elif preco > 0:
        count += 1
        total += preco

    else:
        media = total / count
        formaPgto = int(input("(1 - Dinheiro / 2 - Cartão): "))

        while formaPgto != 1 and formaPgto != 2:
            print('Forma de pgto invalida tente novamente\n')
            formaPgto = int(input("(1 - Dinheiro / 2 - Cartão): "))

        if formaPgto == 1:
            total = total * 0.95

        print(
            f"\nTotal: {total:.2f}\nQtd de produtos: {count}\nMedia: {media:.2f}\nPagamento: {formaPgto}"
            "\n\nFinalizado"
        )

        status = True