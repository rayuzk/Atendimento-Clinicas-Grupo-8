class Clinica():

    def __init__(self, nome, cidade, descricao):
        self.__nome = nome
        self.__cidade = cidade
        self.__descricao = descricao

    @property
    def nome(self):
        return self.__nome

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
