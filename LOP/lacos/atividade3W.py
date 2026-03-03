status = False

while status == False:
    nome = str(input("Digite seu nome de usuario: "))
    senha = str(input("Digite uma senha: "))
    if nome == senha:
        status = False
        print('\nO campo senha nao pode ser igual a nome!!!\n')
    else:
        status = True
        print('\nCriado com sucesso !!!\n')
