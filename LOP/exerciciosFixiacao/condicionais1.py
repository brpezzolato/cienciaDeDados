idade = int(input('Digite a idade do nadador: '))

if idade >=5 and idade <= 12:
    print('Categoria infantil')
elif idade >= 13 and idade <= 17:
    print('Categoria juvenil')
elif idade >= 18:
    print('Categoria adulta')
else:
    print('Idade invalida')