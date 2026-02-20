peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

calc = peso / altura**2

if calc < 18.5:
    print(f"Voce esta abaixo do peso: imc = {calc}")
elif 18.5 <= calc < 25:
    print(f"Voce esta com peso normal: imc = {calc}")
elif 25 <= calc < 30:
    print(f"Voce esta em sobrepeso: imc = {calc}")
else:
    print(f"Voce esta em Obesidade: imc = {calc}")