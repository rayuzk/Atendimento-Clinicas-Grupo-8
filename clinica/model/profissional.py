from model.pessoa import Pessoa

class Profissional(Pessoa):

    def __init__(self, especialidade, registro, nome, celular, cpf):
        super().__init__(nome, celular, cpf)
        self.__especialidade = especialidade
        self.__registro = registro

    @property
    def especialidade(self):
        return self.__especialidade

    @especialidade.setter
    def especialidade(self, especialidade):
        self.__especialidade = especialidade

    @property
    def registro(self):
        return self.__registro
