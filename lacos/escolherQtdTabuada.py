num = int(input("Digite o numero que voce quer saber a tabuada: "))
num = num + 1

for i in range(1, num, 1):
    print(f'\nTabuada do {i}: ')
    for count in range(1, 11, 1):
        resul = count * i
        print(f"{i} x {count} = {resul}")


