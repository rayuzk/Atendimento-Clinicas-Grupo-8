from abc import ABC, abstractmethod

class Pagamento(ABC):
    
    def __init__(self, data, atendimento, paciente, valor_pago ):
        self.__data = data 
        self.__atendimento = atendimento
        self.__paciente = paciente
        self.__valor_pago = valor_pago
        self.__valor_restante = valor_restante

    @property
    def data(self):
        return self.__data
    
    @property
    def atendimento(self):
        return self.__atendimento
    
    @property
    def paciente(self):
        return self.__paciente
    
    @property
    def valor_pago(self):
        if self.valor_pago >= 0:
            return self.__valor_pago
    
    @valor_pago.setter
    def valor_pago(self, valor_pago):
        self.__valor_pago = valor_pago

    
    @property
    def valor_restante(self):
        return self.__valor_restante
    @property
    def valor_restante(self):
        return self.__atendimento.valor - self.__valor_pago
    
    @abstractmethod
    def obter_dados_pagamento(self):
        pass
