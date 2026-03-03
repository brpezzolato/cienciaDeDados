senhaPadro = "palmeiras1914"

while True:
    senhaDigitada = str(input("Digite uma senha: "))

    if senhaDigitada != senhaPadro:
        print("!!! Senha incorreta tente novamente !!!\n")
    else:
        print("\nBem vindo mancha verde !!!\n")
        break