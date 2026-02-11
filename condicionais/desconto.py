valorCompra = float(input("Digite o valor da compra: "))

if valorCompra > 100 and valorCompra < 200:
    conta = valorCompra * 0.9
    print(f"Valor da compra com desconto de 10%: R$ {conta:.2f} (desconto de: R$ {(valorCompra - conta):.2f})")
elif valorCompra > 200 and valorCompra < 500:
    conta = valorCompra * 0.8
    print(f"Valor da compra com desconto de 20%: R$ {conta:.2f} (desconto de: R$ {(valorCompra - conta):.2f})")
elif valorCompra > 500:
    conta = valorCompra * 0.7
    print(f"Valor da compra com desconto de 30%: R$ {conta:.2f} (desconto de: R$ {(valorCompra - conta):.2f})")
else:
    print("Nao elegivel para descontos")