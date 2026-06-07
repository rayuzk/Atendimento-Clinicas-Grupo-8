from model.pessoa import Pessoa

class Paciente(Pessoa):

    def __init__(self, idade, nome, celular, cpf):
        super().__init__(nome, celular, cpf)
        self.__idade = idade

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade
