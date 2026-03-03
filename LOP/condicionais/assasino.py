q1 = input("Telefonou pra vitima? ")
q2 = input("Esteve no local do crime? ")
q3 = input("Mora perto da vitima? ")
q4 = input("Devia para a vitima? ")
q5 = input("Ja trabalhou com a vitima? ")
count = 0

if q1 == "sim":
    count += 1
if q2 == "sim":
    count += 1
if q3 == "sim":
    count += 1
if q4 == "sim":
    count += 1
if q5 == "sim":
    count += 1

# Sim 2 vzs suspeita
# Sim 3 ou 4 cumplice
# Sim 5 assasino
# Resto inocente
if count == 2:
    print("Voce e suspeito", count)
elif count == 3 or count == 4:
    print("Voce e cumplice", count)
elif count == 5:
    print("Voce e o assasino", count)
else:
    print("Inocente", count)
