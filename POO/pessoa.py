from datetime import date #importando apenas a data da biblioteca datetime
class Pessoa:
    #Atributos
    nome = "Fulano"
    idade = 20
    altura = 1.65
    cabelo = "pretos"
    sexo = "M"

    #metodo
    def falar(self, texto):
        print(texto)

    def verificarIdade(self, anoNascimento):
        anoAtual = date.today().year
        resultado = anoAtual - anoNascimento
        print(f"Olá você tem {resultado} anos")

    def pintarCabelo(self, pintar):
        Pessoa.cabelo = pintar
        print(f"Mudou a cor do Cabelo para {pintar}")

#Instanciar um Objeto
alguem = Pessoa()
print(alguem.nome)
alguem.nome = "João"
alguem.sexo = "F"
print(alguem.cabelo)
print(f"Olá {alguem.nome} você possui {alguem.idade} anos")

alguem.falar("Olá hoje o dia está bom para programar")
alguem.verificarIdade(1994)
alguem.pintarCabelo("Rosa")