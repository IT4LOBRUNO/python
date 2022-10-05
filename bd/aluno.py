import pymysql

class Aluno:
    def __init__(self, matricula, nome, nota):
        self.__matricula = matricula
        self.__nome = nome
        self.__nota = nota

    def cadastrarAluno(self):
        conexao = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='turma2_2022'
        )

        comando = "INSERT INTO alunos VALUES(%s, %s, %s)"
        valores = (self.__matricula, self.__nome, self.__nota)

        consulta = conexao.cursor()# cursor irá permitir interação com o banco de dados

        consulta.execute(comando, valores)
        conexao.commit()# irá gravar os dados no banco
        print(f"{consulta.rowcount} linha(s) inserida(s) com sucesso\n\n")

        conexao.close()#fecha a conexao

    def exibirAlunos(self):
        conexao = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='turma2_2022'
        )