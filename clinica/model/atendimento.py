from model.clinica import Clinica
from model.paciente import Paciente
from model.profissional import Profissional
from model.tipo_atendimento import TipoAtendimento

class Atendimento:
    def __init__(
        self,
        clinica,
        paciente,
        profissional,
        data,
        horario_inicio,
        horario_fim,
        tipo_atendimento,
        valor
    ):

        self.__clinica = clinica
        self.__paciente = paciente
        self.__profissional = profissional
        self.__data = data
        self.__horario_inicio = horario_inicio
        self.__horario_fim = horario_fim
        self.__tipo_atendimento = tipo_atendimento
        self.__valor = valor

        self.__procedimentos = []
        self.__pagamentos = [] 

    @property
    def clinica(self):
        return self.__clinica

    @property
    def paciente(self):
        return self.__paciente 
    
    @property
    def profissional(self):
        return self.__profissional 
    
    @property
    def data(self):
        return self.__data 
    
    @property
    def horario_inicio(self):
        return self.__horario_inicio
    
    @property
    def horario_fim(self):
        return self.__horario_fim
    
    @property
    def tipo_atendimento(self):
        return self.__tipo_atendimento
    
    @property
    def valor(self):
        return self.__valor 
    
    @valor.setter
    def valor(self, valor):
        if valor >= 0:
            self.__valor = valor
        
    @property
    def procedimentos(self):
        return self.__procedimentos
    
    @property
    def pagamentos(self):
        return self.__pagamentos


    def adicionar_procedimento(self, procedimento):
        self.__procedimentos.append(procedimento)
    
    def adicionar_pagamento(self, pagamento):
        self.__pagamentos.append(pagamento)

    def calcular_valor_restante(self):
        total_pago = 0
        for pagamento in self.__pagamentos:
            total_pago = total_pago + pagamento.valor_pago
        
        return self.__valor - total_pago

