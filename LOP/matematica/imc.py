altura = float(input("Insira sua altura: "))
peso = float(input("Insira seu peso: "))

imc = peso / (altura * altura)

print("Seu imc e: ", imc)

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso normal')
else:
    print('Acima do peso')
