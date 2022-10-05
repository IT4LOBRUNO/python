from funcionario import Gerente

pessoa2 = Gerente()
r = 0

while r != 3:
    r = float(input("1 - Demitir Funcionário\n2 - Exibir funcionários\n3 - Sair do sistema\n"))
    if r == 1:
        pessoa2.demitir()
    elif r == 2:
        pessoa2.relatorio()
    