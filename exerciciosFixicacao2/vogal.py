frase = input("Digite uma frase ou seu nome completo: ")
count = 0

for i in frase:
    if i in "aeiouAEIOU":
        count += 1

print(count)