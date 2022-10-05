minimo = 1200
def imposto (salario = minimo, imp = 20):
    salario = salario - salario * imp/100
    print(f"seu novo salario é {salario} e foi retirado {imp}%")

valor = float(input("informe seu salário: "))
escolha = input("Deseja informar a porcentagem?(s/n)").lower() #O texto fica minusculo
if escolha == "s":
    impo = float(input("informe o Imposto em porcentagem(sem %): "))
    imposto(valor, impo)
else:
    imposto(valor)