import random
def jogo():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    print(dado1, dado2)
    resultado = 0
    if dado1 + dado2 != resultado:
        if dado1 + dado2 == 7:
            print("Você ganhou!")
        elif dado1 + dado2 == 11:
            print("Você ganhou!")
        elif dado1 + dado2 == 2:
            print("Você perdeu")
        elif dado1 + dado2 == 3:
            print("Você perdeu")
        elif dado1 + dado2 == 12:
            print("Você perdeu")
        else:
            resultado = dado1+dado2
            print(f"Seu ponto: {resultado}")
            cont = 0
            while cont != resultado:
                dado1 = random.randint(1, 6)
                dado2 = random.randint(1, 6)
                cont = dado1 + dado2
                print(cont)
                if cont == 7:
                    cont = resultado
                    print("Você perdeu!")
                elif cont == resultado:
                    print("Você Ganhou!!!")

jogo()