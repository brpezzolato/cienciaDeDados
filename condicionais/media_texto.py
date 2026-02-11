n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

if media >= 7:
    print(f"O aluno foi aprovado com a media {media:.2f}")
else:
    print(f"O aluno foi reprovado com a media {media:.2f}")