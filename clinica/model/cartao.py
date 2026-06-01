class Cartao(Pagamento):
    def __init__(self, data, atendimento, paciente, valor_pago, valor_restante, numero_cartao, bandeira):
        super().__init__(data, atendimento, paciente, valor_pago, valor_restante)
        self.numero_cartao = numero_cartao
        self.bandeira = bandeira 