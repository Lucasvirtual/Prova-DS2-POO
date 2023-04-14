import mysql.connector
from repositories.Repository import Repository

class ProdutoRepository(Repository):


    @staticmethod
    def create(produto):
        # CREATE
        conexao = ProdutoRepository.__criar_conexao()
        cursor = conexao.cursor()

        try:
            comando = f'INSERT INTO produto (nome, custo, categoria, estoque) VALUES ("{produto.nome}",{produto.custo},"{produto.categoria}",{produto.estoque});'
            cursor.execute(comando)
            conexao.commit() # edita o banco de dados

        except "could not convert string to float ":
            print("Digite um valor valido")

        cursor.close()
        conexao.close()

    @staticmethod
    def _read():
        # READ
        conexao = ProdutoRepository.__criar_conexao()
        cursor = conexao.cursor()

        comando = f'SELECT * FROM produto;'
        cursor.execute(comando)
        resultado = cursor.fetchall() # ler o banco de dados
        print(resultado)

        cursor.close()
        conexao.close()


    @staticmethod
    def delete():
        # DELETE
        conexao = ProdutoRepository.__criar_conexao()
        cursor = conexao.cursor()

        comando = f'SELECT * FROM produto'
        cursor.execute(comando)
        resultado = cursor.fetchall()  # ler o banco de dados
        for itens in resultado:
            print(itens)

        delete_produto = input("Qual produto você deseja excluir ? ")
        comando = f'DELETE FROM produto WHERE nome = "{delete_produto}"'
        cursor.execute(comando)
        conexao.commit() # edita o banco de dados

        cursor.close()
        conexao.close()


    @staticmethod
    def update():
        # UPDATE
        conexao = ProdutoRepository.__criar_conexao()
        cursor = conexao.cursor()

        nome_produto = "todynho"
        valor = 6
        comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
        cursor.execute(comando)
        conexao.commit() # edita o banco de dados

        cursor.close()
        conexao.close()


    @staticmethod
    def buscar():
        conexao = ProdutoRepository.__criar_conexao()
        cursor = conexao.cursor()

        buscar = input("Digite o nome do produto que deseja buscar: ")

        comando = f'SELECT * FROM produto WHERE nome ="{buscar}";'
        cursor.execute(comando)
        resultado = cursor.fetchall()  # ler o banco de dados
        print(resultado)

        while True:
            print("1 = adicionar estoque ao produto: ")
            print("2 = remover estoque do produto: ")
            print("3 = voltar ao menu principal")
            opcao = str(input("Qual opção você deseja ? "))

            if opcao == "1":
                estoque_add = int(input("Quanto você quer alocar ? "))
                comando = f'UPDATE produto SET estoque = {estoque_add} WHERE nome = "{buscar}";'
                cursor.execute(comando)
                conexao.commit()


            if opcao == "2":
                estoque_remove = int(input("Quanto você quer retirar ? "))
                comando = f'UPDATE produto SET estoque = {estoque_remove} WHERE nome = "{buscar}";'
                cursor.execute(comando)
                conexao.commit()

            if opcao == "3":
                print(resultado)
                break

        cursor.close()
        conexao.close()


    @staticmethod
    def listar():
        conexao = ProdutoRepository.__criar_conexao()
        cursor = conexao.cursor()

        comando = f'SELECT * FROM produto;'
        cursor.execute(comando)
        resultado = cursor.fetchall()  # ler o banco de dados
        for produtoID,nome,custo,categoria,estoque in resultado:
            print(f"Id: {produtoID}, Nome: {nome}, Custo: {custo}, Categoria: {categoria}, Estoque: {estoque}")
        #for i, buscar in enumerate(resultado):
            #print(f"{i} - {buscar}")
            #não sei a forma que o senhor queria
        cursor.close()
        conexao.close()



    @staticmethod
    def __criar_conexao():
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='prova'
        )
        return conexao

