r = int(input("Quantas pessoas serão cadastradas? "))
x = 0
contador = 0
nome = []
idade = []
if r > 0:
    while x != 3:
        x = int(input("1 - cadastrar um usuário\n2 - Ver usuários cadastrados\n3 - Sair do sistema\n"))
        if x == 1:
            if contador < r:
                name = input("Informe o nome do usuário: ")
                age = int(input("Informe a idade do usuário: "))
                nome.append(name)
                idade.append(age)
                contador += 1
            else: print(f"Todos os {r} usuários, ja forma cadastrados")
        elif x == 2:
            for i in range(0, contador):
                print("nome:",nome[i],"Idade:", idade[i])
print(contador, "Usuários foram cadastrados no sietam")