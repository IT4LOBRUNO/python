class Aluno: # metodo contrutor
    def __init__(self, nome = "Fulano", matricula = 0, genero = "N"):
        self.nome = nome
        self.matricula = matricula
        self.genero = genero
        

    def exibirDados(self):
        print(f"O aluno {self.nome} possui a matricula {self.matricula}  e é do gênero {self.genero}")
