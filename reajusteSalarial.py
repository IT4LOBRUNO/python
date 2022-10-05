salario = float(input("Informe o Salário: "))
if salario < 500:
    salario = salario - salario * 0.15
elif salario <= 1000:
    salario = salario - salario * 0.1
else:
    salario = salario - salario * 0.05
print(salario)