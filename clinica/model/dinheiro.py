from model.pagamento import Pagamento 

class Dinheiro(Pagamento):
    def __init__(self, data, atendimento, paciente, valor_pago):
        super().__init__(data, atendimento, paciente, valor_pago)
    
    def obter_dados_pagamento(self):
        return "Pagamento realizado em dinheiro"