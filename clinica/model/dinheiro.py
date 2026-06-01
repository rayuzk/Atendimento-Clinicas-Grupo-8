class Dinheiro(Pagamento):
    def __init__(self, data, atendimento, paciente, valor_pago, valor_restante):
        super().__init__(data, atendimento, paciente, valor_pago, valor_restante)