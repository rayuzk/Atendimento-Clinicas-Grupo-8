'''
class TelaTipoAtendimento:

    def __init__(self, controlador_sistema):
        self.controlador_sistema = controlador_sistema

    def obter_dados_tipo_atendimento(self):
        descricao = input("Descrição: ")
        return {"descricao": descricao}

    def mostrar_tipos_atendimento(self, tipos_atendimento):
        if len(tipos_atendimento) == 0:
            print("Nenhum tipo de atendimento cadastrado.")
            return
        for i in range(len(tipos_atendimento)):
            print(i, "-", tipos_atendimento[i].descricao)

    def abrir_tela(self):
        while True:
            print("\nMenu Tipo de Atendimento")
            print("(1) Incluir tipo de atendimento")
            print("(2) Listar tipos de atendimento")
            print("(3) Alterar tipo de atendimento")
            print("(4) Excluir tipo de atendimento")
            print("(5) Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                dados = self.obter_dados_tipo_atendimento()
                try:
                    self.controlador_sistema.controlador_tipo_atendimento.incluir_tipo_atendimento(
                        dados["descricao"]
                    )
                    print("Tipo de atendimento cadastrado com sucesso!")
                except ValueError as e:
                    print("Erro:", e)

            elif opcao == "2":
                tipos = self.controlador_sistema.controlador_tipo_atendimento.listar_tipos_atendimento()
                self.mostrar_tipos_atendimento(tipos)

            elif opcao == "3":
                descricao = input("Descrição atual: ")
                nova_descricao = input("Nova descrição: ")
                try:
                    self.controlador_sistema.controlador_tipo_atendimento.alterar_tipo_atendimento(
                        descricao, nova_descricao
                    )
                    print("Tipo de atendimento alterado com sucesso!")
                except ValueError as e:
                    print("Erro:", e)

            elif opcao == "4":
                descricao = input("Descrição do tipo a excluir: ")
                try:
                    self.controlador_sistema.controlador_tipo_atendimento.excluir_tipo_atendimento(descricao)
                    print("Tipo de atendimento excluído com sucesso!")
                except ValueError as e:
                    print("Erro:", e)

            elif opcao == "5":
                break

            else:
                print("Opção inválida!")
'''
