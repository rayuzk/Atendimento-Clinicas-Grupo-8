'''
class TelaPaciente:

    def __init__(self, controlador_sistema):
        self.controlador_sistema = controlador_sistema

    def obter_dados_paciente(self):
        nome = input("Nome: ")
        celular = input("Celular: ")
        cpf = input("CPF: ")
        idade = int(input("Idade: "))
        return {
            "nome": nome,
            "celular": celular,
            "cpf": cpf,
            "idade": idade
        }

    def mostrar_pacientes(self, pacientes):
        if len(pacientes) == 0:
            print("Nenhum paciente cadastrado.")
            return
        for i in range(len(pacientes)):
            print(i, "-", pacientes[i].nome, "|", pacientes[i].cpf)

    def abrir_tela(self):
        while True:
            print("\nMenu Pacientes")
            print("(1) Incluir paciente")
            print("(2) Listar pacientes")
            print("(3) Alterar paciente")
            print("(4) Excluir paciente")
            print("(5) Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                try:
                    dados = self.obter_dados_paciente()
                    self.controlador_sistema.controlador_paciente.incluir_paciente(
                        dados["idade"],
                        dados["nome"],
                        dados["celular"],
                        dados["cpf"]
                    )
                    print("Paciente cadastrado com sucesso!")
                except ValueError as e:
                    print("Erro:", e)

            elif opcao == "2":
                pacientes = self.controlador_sistema.controlador_paciente.listar_pacientes()
                self.mostrar_pacientes(pacientes)

            elif opcao == "3":
                cpf = input("CPF do paciente a alterar: ")
                novo_nome = input("Novo nome: ")
                novo_celular = input("Novo celular: ")
                try:
                    nova_idade = int(input("Nova idade: "))
                    self.controlador_sistema.controlador_paciente.alterar_paciente(
                        cpf, novo_nome, novo_celular, nova_idade
                    )
                    print("Paciente alterado com sucesso!")
                except ValueError as e:
                    print("Erro:", e)

            elif opcao == "4":
                cpf = input("CPF do paciente a excluir: ")
                try:
                    self.controlador_sistema.controlador_paciente.excluir_paciente(cpf)
                    print("Paciente excluído com sucesso!")
                except ValueError as e:
                    print("Erro:", e)

            elif opcao == "5":
                break

            else:
                print("Opção inválida!")
'''

