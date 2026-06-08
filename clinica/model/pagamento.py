from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, data, atendimento, paciente, valor_pago):
        self.__data = data 
        self.__atendimento = atendimento
        self.__paciente = paciente
        self.__valor_pago = valor_pago

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
        return self.__valor_pago 
    
    @valor_pago.setter
    def valor_pago(self, valor_pago): self.__valor_pago = valor_pago

    @property
    def valor_restante(self):
        return self.__atendimento.valor - self.__valor_pago
    
    @abstractmethod
    def obter_dados_pagamento(self):
        pass

class Dinheiro(Pagamento):
    def __init__(self, data, atendimento, paciente, valor_pago):
        super().__init__(data, atendimento, paciente, valor_pago)
    
    def obter_dados_pagamento(self):
        return "Pagamento realizado em dinheiro"

class Pix(Pagamento):
    def __init__(self, data, atendimento, paciente, valor_pago, cpf):
        super().__init__(data, atendimento, paciente, valor_pago)
        self.__cpf = cpf
    
    @property
    def cpf(self): 
        return self.__cpf
    
    def obter_dados_pagamento(self):
        return f"Pagamento realizado via pix, cpf do pagador: {self.cpf}"

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
        return f"Pagamento realizado em cartão, bandeira: {self.bandeira}"