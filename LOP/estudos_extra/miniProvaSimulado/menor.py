count = 1

while count <= 7:
    num = float(input(f'N{count})Digite um numero: '))
    if count == 1:
        menor = num
    if num < menor:
        menor = num
    count += 1

print(f'O menor numero é: {menor}')


for i in range(5):
    num = float(input(f'N{i + 1})Digite um numero: '))
    if i == 0:
        menor = num
    if num < menor:
        menor = num

print(f'O menor numero é: {menor}')
