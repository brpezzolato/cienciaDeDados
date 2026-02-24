inteiro = int(input("Digite um numero inteiro: "))
status = True

for i in range(2, inteiro):
    if inteiro % i == 0:
        status = False


if status == False or inteiro == 0 or inteiro == 1 or inteiro < 0:
    print("NN eh primo")
else:
    print("primo")
