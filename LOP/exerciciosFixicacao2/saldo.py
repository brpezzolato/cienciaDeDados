saldo = 500.0

while True:
    print('(1) Depositar, (2) Sacar e (3) Sair')
    opcao = int(input('Digite a opção: '))
    if opcao == 1:
        valorAdd = float(input('\nQuanto vc quer adicionar: '))
        saldo += valorAdd
        print(f'\nNovo saldo: {saldo}\n')
    elif opcao == 2:
        valorSub = float(input('\nQuanto vc quer retirar: '))
        if valorSub > saldo:
            print('\nSaldo Insuficiente !!!')
        else:
            saldo -= valorSub
            print(f'\nNovo saldo: {saldo}')
    elif opcao == 3:
        print(f'\nSaldo final: {saldo}')
        break
    else:
        print('Opcao invalida !!!')