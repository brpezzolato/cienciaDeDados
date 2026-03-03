somaPar = 0
somaImpar = 0

for i in range(10):
    num = float(input(f'{i + 1}) Digite um numero: '))

    if num % 2 == 0:
        somaPar += num
    else:
        somaImpar += num

print(f'Soma dos Pares: {somaPar}')
print(f'Soma dos Impares: {somaImpar}')