inteiro = int(input("Digite um numero inteiro: "))
soma = 0

for i in range(1, inteiro):
    if inteiro % i == 0:
        soma += i
    else:
        continue

if soma == inteiro:
    print(f'E um numero perfeito, soma dos divisores {soma}')
else:
    print(f'Nao e um numero perfeito, soma dos divisores {soma}')
