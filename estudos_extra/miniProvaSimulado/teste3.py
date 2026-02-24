num = int(input("Digite um numero: "))
count = 0

if num == 0:
    print(1)
else:
    while True:
        if num != 0:
            num = num // 10
            count += 1
        else:
            break

    print(count)
