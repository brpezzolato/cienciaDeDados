for i in range(5):
    num = float(input("Digite um numero: "))
    if i == 0:
        maior = num
        posicao = i + 1
    elif num > maior:
        maior = num
        posicao = i + 1

print(f"O {posicao}° numero ({maior}) e o maior !!!!")
