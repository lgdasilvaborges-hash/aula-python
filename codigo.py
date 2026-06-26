compra_1 = 50.00
compra_2 = 150.00
compra_3 = 300.00
repetir = "S"
while repetir == "S":
    nome_cliente = input("nome do cliente: ")
    valorcompra = float(input("valor da compra: R$ "))
    if valorcompra > 100:
        desconto = valorcompra * 0.10
    else:
        desconto = 0
    valorfinal = valorcompra - desconto
    print("\ncliente:", nome_cliente)
    print("desconto: R$", desconto)
    print("valor final: R$",valorfinal)
    repetir = input("\n deseja realizar outro atendimento? (S/n)").upper()
print("programa encerrado.")
