conquistas = 0


def passo2():
    print("- Condicao de exploracao (passo 2)")

    while True:
        res = input(
            "Explorador voce observa algm obstaculo no caminho (1- para sim, 2- para nao) ??? "
        )
        if res == "1" or res == "2":
            break
        else:
            print("Resposta nao valida (1- para sim, 2- para nao)\n")

    return res


def passo3():
    print("\n- Superar obstaculo (passo 3)")

    while True:
        res = input(
            "Explorador voce vai escalar ou contornar a montanha (1- para escalar , 2- para contornar) ??? "
        )
        if res == "1" or res == "2":
            break
        else:
            print("Resposta nao valida (1- para escalar , 2- para contornar)\n")

    return res


def passo4():
    print("\n- Escalada da montanha (passo 4)")

    while True:
        res = input("Explorador voce obteve sucesso (1- para sim , 2- para nao) ??? ")
        if res == "1" or res == "2":
            break
        else:
            print("Resposta nao valida (1- para sim , 2- para nao)\n")
    return res


def passo5():
    return print(
        "A equipe contorna a montanha com sucesso e continua a exploração (passo 5)"
    )


def passo6():
    print("\n- Condição Científica (passo 6)")

    while True:
        res = input(
            "Explorador encontrou area rica de minerais ou sinal de vida (1- para sim , 2- para nao) ??? "
        )
        if res == "1" or res == "2":
            break
        else:
            print("Resposta nao valida (1- para sim , 2- para nao)\n")
    return res


def passo7(conquistas):
    print("Coleta de Dados Científicos (passo 7)")

    qtd = int(input("Quantas coletas de minerios foram feitas? "))

    for i in range(qtd):
        minerios = int(input(f"Quantos minerios foram coletados na coleta {i+1}? "))
        conquistas += minerios

    return conquistas


def passo8():
    print("\n- Condição Científica (passo 6)")

    while True:
        res = input(
            "Explorador desejar continuar a exploração ou retornar a nave (1- para continuar , 2- para retornar) ??? "
        )
        if res == "1" or res == "2":
            break
        else:
            print("Resposta nao valida (1- para sim , 2- para nao)\n")
    return res


def passo9():
    return print(
        "A tripulação retorna à Exploradora Estelar e parte de volta para a Terra,trazendo consigo as descobertas incríveis feitas durante a expedição."
    )


print(
    "\nEm um futuro distante, a humanidade alcançou as estrelas e iniciou a exploração de planetas distantes. A bordo da nave intergaláctica "
    "Exploradora Estelar"
    " uma tripulação composta por cientistas, engenheiros e aventureiros chega ao planeta Alphara-7, um mundo misterioso repleto de paisagens alienígenas.\n"
)

print("-" * 150)

print(
    "\nAo aterrissar em Alphara-7, a tripulação sente a expectativa no ar.Equipados com trajes espaciais avançados, eles começam a explorar a superfície do planeta, ansiosos por desvendar seus segredos \n"
)

while True:
    respostaPasso2 = passo2()

    if respostaPasso2 == "1":
        while True:
            respostaPasso3 = passo3()
            if respostaPasso3 == "1":
                respostaPasso4 = passo4()
                if respostaPasso4 == "1":
                    print("Explorador sucesso ao escalar a montanha\n")
                    break
                else:
                    print(
                        "Explorador nao conseguiu escalar tente novamente ou outro caminho\n"
                    )
            else:
                passo5()
                break
    else:
        respostaPasso6 = passo6()

        if respostaPasso6 == "1":
            conquistas = passo7(conquistas)
            print(f"Seus minerios/conquistas foram {conquistas} unidades\n")

            decisao = passo8()

            if decisao == "1":
                continue
            else:
                passo9()
                print(f"\nTotal de conquistas obtidas: {conquistas} unidades")
                break
        else:
            continue
