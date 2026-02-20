num = int(input('Tabuada do ???: '))

print(f'\nTabuada do {num}:')
for count in range(1, 11, 1):
    print(f'{num} x {count} = {num * count}')