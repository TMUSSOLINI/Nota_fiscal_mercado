class Produto:
    def __init__(self, nome, marca, preco, quantidade):
        self.__nome = nome
        self.__marca = marca
        self.__preco = preco
        self.__quantidade = quantidade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def preco(self):
        return self.__preco

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    def extrato(self):
        return self.nome, self.quantidade, self.preco
