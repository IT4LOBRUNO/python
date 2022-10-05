num = int(input("Informe um número: "))
resultado = 0
if num == 0:
    resultado = 0
    print(resultado)
elif num > 0:
    for i in range (num):
        resultado = num * num
    print(resultado)
else:
    for i in range(-num):
        resultado = num * num
    print(resultado)