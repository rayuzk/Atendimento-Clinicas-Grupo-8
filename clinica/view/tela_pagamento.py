class TelaPagamento:
    
    def __init__(self, controlador_sistema):
        self.controlador_sistema = controlador_sistema

    def entra_dados_pagamento(self):
        data = input("Digite a data: ")
        atendimento = input("Digite o atendimento: ")
        paciente = input("Digite o nome do paciente: ")
        valor_pago = float(input("Digite o valor pago: "))
        tipo_pagamento = input("Digite o tipo de pagamento: ")

        cpf = None
        numero_cartao = None
        bandeira = None

        if tipo_pagamento == "pix":
            cpf = input("Digite o CPF: ")

        elif tipo_pagamento == "cartao":
            numero_cartao = input("Digite o número do cartão: ")
            bandeira = input("Digite a bandeira: ")

        return {
            "data": data,
            "atendimento": atendimento,
            "paciente": paciente,
            "valor_pago": valor_pago,
            "tipo_pagamento": tipo_pagamento,
            "cpf": cpf,
            "numero_cartao": numero_cartao,
            "bandeira": bandeira
        }

    def mostrar_pagamentos(self):
        pagamentos = self.controlador_sistema.controlador_pagamento.listar_pagamentos()

        if len(pagamentos) == 0:
            print("Nenhum pagamento cadastrado.")
            return

        for pagamento in pagamentos:
            print("Data:", pagamento.data)
            print("Paciente:", pagamento.paciente)
            print("Valor pago:", pagamento.valor_pago)
            print("Tipo:", pagamento.tipo_pagamento)

    def abrir_tela(self):

        while True:
            print("\n Menu Pagamento")
            print("(1) Incluir pagamento")
            print("(2) Listar pagamentos")
            print("(3) Voltar")

            opcao = input("Escolha: ")

            if opcao == "1":
                dados = self.entra_dados_pagamento()

                self.controlador_sistema.controlador_pagamento.incluir_pagamento(
                    dados["data"],
                    dados["atendimento"],
                    dados["paciente"],
                    dados["valor_pago"],
                    dados["tipo_pagamento"],
                    dados["cpf"],
                    dados["numero_cartao"],
                    dados["bandeira"]
                )

                print("Pagamento registrado com sucesso!")

            elif opcao == "2":
                self.mostrar_pagamentos()

            elif opcao == "3":
                break

            else:
                print("Opção inválida!")