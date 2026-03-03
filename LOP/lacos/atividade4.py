soma = 0

for i in range(5):
    num = float(input("Digite um numero: "))
    soma += num
    if i > 0:
        media = soma / (i + 1)

print(f"A soma deles e: {soma} e a media e: {media}")