
class Produto():
    def __init__(self,nome, custo, categoria, estoque = 0):
        self._nome = nome
        self._custo = custo
        self._categoria = categoria
        self.estoque = estoque

    def __str__(self):
        return f"Nome: {self.nome}, Custo: {self.custo}, Categoria: {self.categoria}, Estoque: {self.estoque}"


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):

        self._nome = novo_nome.upper()
        if novo_nome == "":
            print("Nome não pode ser vazio")
        else:
            raise ValueError('Nome de produto inválido')


    @property
    def custo(self):
        return self._custo

    @custo.setter
    def custo(self, novo_custo):
        self._custo = novo_custo()
        if novo_custo > 0:
            print("Custo não pode ser um valor negativo")
        else:
            raise ValueError('Custo inválido')


    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, nova_categoria):
        self._categoria = nova_categoria.upper()
        if nova_categoria == "":
            print("Categoria não pode ser um valor vazio")
        else:
            raise ValueError('Nome de categoria inválido')


    def consultar_estoque(self,estoque):
        return f"A quantidade de estoque é {estoque}"


    def alterar_estoque(self,estoque):
        alterar_estoque = int(input("Quanto adicionar ? "))
        estoque = alterar_estoque
        print(estoque)