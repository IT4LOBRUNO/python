class Conta:
    def __init__(self, numero = 0,titular = "Pessoa", saldo = 1000):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo

    def relatorio(self):
        print(f"Olá {self.__titular}, o número da sua conta é {self.__numero} e seu saldo é {self.__saldo}")
    
    def sacar(self, valor):
        if valor > self.__saldo:
            print(f"Saldo insuficiente, seu saldo é {self.__saldo}") 
        elif valor <= 0:
            print(f"Você não pode sacar esse valor {valor}")
        else:
            self.__saldo = self.__saldo - valor
            print(f"Voce sacou {valor}\n")

    def depositar(self, valor):
        if valor <= 0:
            print(f"Você não pode depositar esse valor {valor}")
        else:
            self.__saldo = self.__saldo + valor
            print(f"Você depositou {valor}\n")

    def getSaldo(self):
        print(f"Olá seu saldo atual é {self.__saldo}\n")