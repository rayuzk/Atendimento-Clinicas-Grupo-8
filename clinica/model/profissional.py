class Profissional(Pessoa):
    def __init__(self, especialidade, registro, nome, celular, cpf):
        super().__init__(nome, celular, cpf)
        self.especialidade = especialidade
        self.registro = registro