'''
class TelaPagamento:

    def __init__(self, controlador_sistema):
        self.controlador_sistema = controlador_sistema

    def entra_dados_pagamento(self):
        print("\nAtendimentos disponíveis:")
        atendimentos = self.controlador_sistema.controlador_atendimento.listar_atendimentos()

        if len(atendimentos) == 0:
            print("Nenhum atendimento cadastrado.")
            return None

        for i in range(len(atendimentos)):
            print(i, "-", atendimentos[i].paciente.nome, "|", atendimentos[i].data)

        indice = int(input("Escolha o índice do atendimento: "))
        atendimento = atendimentos[indice]
        paciente = atendimento.paciente

        data = input("Data do pagamento (dd/mm/aaaa): ")
        valor_pago = float(input("Valor pago: "))

        print("Tipo de pagamento: (1) DINHEIRO  (2) PIX  (3) CARTAO")
        escolha = input("Escolha: ")

        cpf = None
        numero_cartao = None
        bandeira = None

        if escolha == "1":
            tipo_pagamento = "DINHEIRO"
        elif escolha == "2":
            tipo_pagamento = "PIX"
            cpf = input("CPF do pagador: ")
        elif escolha == "3":
            tipo_pagamento = "CARTAO"
            numero_cartao = input("Número do cartão: ")
            bandeira = input("Bandeira: ")
        else:
            print("Tipo inválido.")
            return None

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

    def mostrar_pagamentos(self, pagamentos):
        if len(pagamentos) == 0:
            print("Nenhum pagamento cadastrado.")
            return
        for pagamento in pagamentos:
            print("Data:", pagamento.data)
            print("Paciente:", pagamento.paciente.nome)
            print("Valor pago: R$", pagamento.valor_pago)
            print(pagamento.obter_dados_pagamento())
            print("---")

    def abrir_tela(self):
        while True:
            print("\nMenu Pagamento")
            print("(1) Incluir pagamento")
            print("(2) Listar pagamentos")
            print("(3) Voltar")

            opcao = input("Escolha: ")

            if opcao == "1":
                try:
                    dados = self.entra_dados_pagamento()
                    if dados is None:
                        continue
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
                except ValueError as e:
                    print("Erro:", e)

            elif opcao == "2":
                pagamentos = self.controlador_sistema.controlador_pagamento.listar_pagamentos()
                self.mostrar_pagamentos(pagamentos)

            elif opcao == "3":
                break

            else:
                print("Opção inválida!")
'''
