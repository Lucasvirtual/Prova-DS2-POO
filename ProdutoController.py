from entities.Produto import Produto
from repositories.ProdutoRepository import ProdutoRepository

class ProdutoController:

    @staticmethod
    def exibir_menu():
        try:
            print('---------- MENU ----------')
            print('1 - CADASTRAR PRODUTO')
            print('2 - LISTAR TODOS OS PRODUTOS ')
            print('3 - BUSCAR PRODUTO')
            print('4 - EXCLUIR PRODUTO')
            print('5 - SAIR DO PROGRAMA')
            opcao = int(input('Digite o número da operação desejada: '))
            if opcao == 1:
                ProdutoController.cadastrar_produto()
            elif opcao == 2:
                ProdutoController.listar_produtos()
            elif opcao == 3:
                ProdutoController.buscar_produto()
            elif opcao == 4:
                ProdutoController.excluir_produto()
            elif opcao == 5:
                return False
            else:
                raise ValueError('Opção inválida')
        except ValueError as erro:
            print(erro)
        return True




    @staticmethod
    def cadastrar_produto():
        '''
        Método estático que deve solicitar ao usuário os dados necessários para cadastrar um Produto, em seguida
        deverá solicitar que o repositorio realize a insersão do produto no banco de dados. Este método deverá fazer
        o tratamento de exceções geradas pela entrada inconsistente de dados pelo usuário (basta exibir o texto da
        exceção).
        '''
        nome = input("Digite o nome do produto: ")
        custo = float(input("Digite o custo do produto: "))
        categoria = input("Digite a categoria do produto: ")

        nome = Produto(nome,custo,categoria)

        ProdutoRepository.create(nome)

    @staticmethod
    def listar_produtos():
        '''
        Método estático que deve solicitar que o repositorio realize uma consulta de todos os Produtos cadastrados
        no banco de dados. Listando cada produto e seu respectivo indice na lista de produtos recebida pelo repositorio.
        '''
        ProdutoRepository.listar()


    @staticmethod
    def buscar_produto():
        '''
        Método estático que deve solicitar ao usuário o nome de um Produto e solicitar que o repositorio realize uma
        consulta no banco de dados para buscar as informações deste produto. Em seguida, deve exibir ao usuário,
        as opções de ADICIONAR AO ESTOQUE e de REMOVER DO ESTOQUE, que, atraves do repositorio, adicionam ou remover
        quantidades do estoque daquele produto buscado. Este método deverá fazer o tratamento de exceções geradas pela
        entrada inconsistente de dados pelo usuário (basta exibir o texto da exceção).
        '''
        ProdutoRepository.buscar()


    @staticmethod
    def excluir_produto():
        '''
        Método estático que deve solicitar ao usuario o nome de um Produto, pedir que o repositorio busque por este
        produtro no banco, e caso o produto exista no banco de dados, deverá realize a remoção do produto no banco de
        dados. Este método deverá fazer o tratamento de exceções geradas através entrada inconsistente de dados pelo
        usuário (basta exibir o texto da exceção).
        '''
        ProdutoRepository.delete()