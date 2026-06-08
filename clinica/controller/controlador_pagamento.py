from model.pagamento import Dinheiro, Pix, Cartao

class ControladorPagamento:

    def __init__(self, controlador_sistema):
        self.controlador_sistema = controlador_sistema
        self.pagamentos = []

    def incluir_pagamento(
        self,
        data,
        atendimento,
        paciente,
        valor_pago,
        tipo_pagamento,
        cpf=None,
        numero_cartao=None,
        bandeira=None
    ):
        if atendimento is None:
            raise ValueError("Atendimento inválido.")

        if paciente is None:
            raise ValueError("Paciente inválido.")

        if valor_pago <= 0:
            raise ValueError("Valor inválido.")

        if tipo_pagamento is None:
            raise ValueError("Tipo de pagamento inválido.")

        if tipo_pagamento == "PIX" and cpf is None:
            raise ValueError("CPF obrigatório para pagamento via PIX.")

        if tipo_pagamento == "CARTAO" and (numero_cartao is None or bandeira is None):
            raise ValueError("Número do cartão e bandeira são obrigatórios.")

        if tipo_pagamento == "DINHEIRO":
            pagamento = Dinheiro(data, atendimento, paciente, valor_pago)

        elif tipo_pagamento == "PIX":
            pagamento = Pix(data, atendimento, paciente, valor_pago, cpf)

        elif tipo_pagamento == "CARTAO":
            pagamento = Cartao(data, atendimento, paciente, valor_pago, numero_cartao, bandeira)

        else:
            raise ValueError("Tipo de pagamento inválido. Use DINHEIRO, PIX ou CARTAO.")

        self.pagamentos.append(pagamento)
        atendimento.adicionar_pagamento(pagamento)
        return pagamento

    def listar_pagamentos(self):
        return self.pagamentos

    def abrir_tela(self):
        self.controlador_sistema.tela_sistema.abrir_tela_pagamento()
