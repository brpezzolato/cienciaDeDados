num = int(input("Digite um numero: "))
fatorial = 1

for i in range(1, num + 1):
    fatorial *= i

if fatorial % 2 == 0:
    print(f"Fatorial de {num} é {fatorial} (Par)")
else:
    print(f"Fatorial de {num} é {fatorial} (Impar)")
