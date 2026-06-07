from model.pagamento import Pagamento

class ControladorPagamento:
    def __init__(self):
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
            print("Atendimento inválido")
            return

        if paciente is None:
            print("Paciente inválido")
            return

        if valor_pago <= 0:
            print("Valor inválido")
            return

        if tipo_pagamento is None:
            print("Tipo de pagamento inválido")
            return

        
        if tipo_pagamento == "PIX" and cpf is None:
            print("CPF obrigatório para PIX")
            return

        if tipo_pagamento == "CARTAO" and (numero_cartao is None or bandeira is None):
            print("Dados do cartão inválidos")
            return

        pagamento = Pagamento(
            data,
            atendimento,
            paciente,
            valor_pago,
            tipo_pagamento,
            cpf,
            numero_cartao,
            bandeira
        )

        self.pagamentos.append(pagamento)
        atendimento.adicionar_pagamento(pagamento)

        print("Pagamento registrado")

    def listar_pagamentos(self):
        return self.pagamentos

    def abrir_tela(self):
        pass