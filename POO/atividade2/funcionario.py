import pymysql

class Funcionario:
    def __init__(self, nome = "Generico", id = 123, funcao = "Empregado", salario = 1296.00, genero = "N"):
        self.__nome = nome
        self.__id = id
        self.__funcao = funcao
        self.__salario = salario
        self.__genero = genero

    def relatorio(self):
        conexao = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='funcionario'
        )
        
        comando = "SELECT * FROM func"
        consulta = conexao.cursor()
        consulta.execute(comando)
        resultado = consulta.fetchall()

        print(resultado)

    def cadastro(self):
        conexao = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='funcionario'
        )

        comando = "INSERT INTO func VALUES(%s, %s, %s, %s, %s)"

        self.__nome = input("Qual o nome do funcionário? ")
        self.__id = int(input("Qual o número de identificação deste funcionário? "))
        self.__funcao = input("Qual o cargo deste funcionário? ")
        self.__salario = float(input("Qual o salário deste funcionário? "))
        self.__genero = input("Qual o genero deste funcionário? ")

        valores = (self.__nome, self.__id, self.__funcao, self.__salario, self.__genero)

        consulta = conexao.cursor()# cursor irá permitir interação com o banco de dados

        consulta.execute(comando, valores)
        conexao.commit()# irá gravar os dados no banco
        print(f"{consulta.rowcount} linha(s) inserida(s) com sucesso\n\n")

        conexao.close()#fecha a conexao


    def promo(self):
        conexao = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='funcionario'
        )

        comando = "UPDATE func SET salario = (%s) WHERE id = (%s)"

        self.__id = input("Qual o ID do funcionário? ")
        self.__funcao = input("Qual o novo cargo deste funcionário ")
        self.__salario = float(input("Qual o novo salário deste funcionário? "))

        valores = (self.__salario, self.__id)

        consulta = conexao.cursor()

        consulta.execute(comando, valores)
        conexao.commit()
        print("Mudança realizada com sucesso" , valores)

        conexao.close()
        

class Gerente(Funcionario):
    def __init__(self, contato = "Nº Gerente", gerencia = "Ordens"):
        self.__contato = contato
        self.__gerencia = gerencia
    
    def demitir(self):
        conexao = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='funcionario'
        )

        comando = "DELETE FROM func WHERE id = (%s)"

        self.__id = input("Qual o ID do funcionário que será demitido? ")

        valores = (self.__id)

        consulta = conexao.cursor()

        consulta.execute(comando, valores)
        conexao.commit()
        print("Funcionário removido do sistema!")
        conexao.close()

    def relatorio(self):
        conexao = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='funcionario'
        )
        
        comando = "SELECT * FROM func"
        consulta = conexao.cursor()
        consulta.execute(comando)
        resultado = consulta.fetchall()

        print(resultado)

