num = int(input('Digite um numero: '))
soma = 0

for i in range(1, num + 1):
    if i % 3 == 0:
        soma += i

print(f'A soma dos divisiveis de 3 ate {num} e: {soma}')