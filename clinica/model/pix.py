class Pix(Pagamento):
    def __init__(self, data, atendimento, paciente, valor_pago, valor_restante, cpf):
        super().__init__(data, atendimento, paciente, valor_pago, valor_restante)
        self.cpf = cpf