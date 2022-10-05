from conta import Conta

cliente = Conta()


r = 0
while r!=4:
    print("Menu\n1-Sacar\n2-Depositar\n3-Saldo\n4-Sair")
    r = float(input("Escolha uma opção "))
    if r == 1:
        valor = float(input("Qual o valor a ser sacado? "))
        cliente.sacar(valor)

    elif r == 2:
        valor = float(input("Qual o valor a ser depositado? "))
        cliente.depositar(valor)

    elif r == 3:
        cliente.getSaldo()
