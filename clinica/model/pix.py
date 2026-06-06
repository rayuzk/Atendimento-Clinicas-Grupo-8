from model.pagamento import Pagamento

class Pix(Pagamento):
    def __init__(self, data, atendimento, paciente, valor_pago, cpf):
        super().__init__(data, atendimento, paciente, valor_pago)
        self.__cpf = cpf

    @property
    def cpf(self):
        return self.__cpf
    

    def obter_dados_pagamento(self):
        return f'Pagamento realizado via pix, cpf do pagador: {self.cpf}'