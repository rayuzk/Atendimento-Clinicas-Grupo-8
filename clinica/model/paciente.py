class Paciente(Pessoa):
    def __init__(self, idade, nome, celular, cpf):
        super().__init__(nome, celular, cpf)
        self.idade = idade