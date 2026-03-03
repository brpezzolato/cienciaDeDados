num1 = int(input("Digite o primeiro numero (inicio): "))
num2 = int(input("Digite o segundo numero (fim): "))

if num1 <= num2:
    increment = 1
else:
    increment = -1

for i in range(num1, num2 + 1, increment):
    print(i)