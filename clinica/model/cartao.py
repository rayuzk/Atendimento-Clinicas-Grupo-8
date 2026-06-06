from model.pagamento import Pagamento

class Cartao(Pagamento):
    def __init__(self, data, atendimento, paciente, valor_pago, numero_cartao, bandeira):
        super().__init__(data, atendimento, paciente, valor_pago)
        self.__numero_cartao = numero_cartao
        self.__bandeira = bandeira 
    
    @property
    def numero_cartao(self):
        return self.__numero_cartao
    
    @property
    def bandeira(self):
        return self.__bandeira
    
    def obter_dados_pagamento(self):
        return f'Pagamento realizado em cartão, bandeira: {self.bandeira}'