from aluno import Aluno

matricula = int(input("Informe a matricula: "))
nome = input("Informe o nome do Aluno: ")
nota = float(input("Informe a nota do aluno: "))

aluno1 = Aluno(matricula, nome, nota)
aluno1.cadastrarAluno()
