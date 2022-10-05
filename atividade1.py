salarioBruto = float(input("Informe o Sálario "))
salario = salarioBruto - (salarioBruto * (0.1))
salarioLiquido = salario - (salario * (0.05))
print("Seu Salário é {}\nCom a redução da previdência fica {}\nCom a redução de impostos você receberá apenas {} triste fim!".format(salarioBruto, salario, salarioLiquido))