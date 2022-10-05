from funcionario import Funcionario

pessoa = Funcionario()
r = 0

while r != 4:
    r = float(input("1 - Cadastrar novo funcionário\n2 - Checar funcionário cadastrado\n3 - promover funcionário\n4 - Sair do sistema\n"))
    if r == 1:
        pessoa.cadastro()
    elif r == 2:
        pessoa.relatorio()
    elif r == 3:
        pessoa.promo()
