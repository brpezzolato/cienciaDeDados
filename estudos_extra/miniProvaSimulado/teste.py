usuarios = ["admin", "bruno", "carla", "senai"]
status = False

while status == False:
    nome = input("Digite seu nome de usuario: ")
    if nome is None:
        print("Tente dnv nn pode ser nulo")
    else:
        if nome in usuarios:
            print("Acesso permitido !")
            status = True
        else:
            print("Tente dnv")
