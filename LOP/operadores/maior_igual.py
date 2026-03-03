num1 = float(input("Digite um numero: "))
num2 = float(input("Digite um numero: "))

print(num1 > num2 and f"O numero {num1} e maior" or num1 < num2 and f"O numero {num2} e maior" or num1 == num2 and 'O numeros sao iguais')