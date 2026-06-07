class TelaSistema:
    def __init__(self, controlador_sistema):
        self.controlador_sistema = controlador_sistema

    def abrir_tela(self):

        while True:
            print("\nBem-vindo ao menu principal, selecione a opção desejada :)")
            print("(1) Clínicas")
            print("(2) Pacientes")
            print("(3) Profissionais")
            print("(4) Tipo de atendimento")
            print("(5) Atendimentos")
            print("(6) Pagamentos")
            print("(7) Sair")

            opcao = input("Minha escolha é a opção: ")

            if opcao == "1":
                self.controlador_sistema.controlador_clinica.abrir_tela()

            elif opcao == "2":
                self.controlador_sistema.controlador_paciente.abrir_tela()

            elif opcao == "3":
                self.controlador_sistema.controlador_profissional.abrir_tela()

            elif opcao == "4":
                self.controlador_sistema.controlador_tipo_atendimento.abrir_tela()

            elif opcao == "5":
                self.controlador_sistema.controlador_atendimento.abrir_tela()

            elif opcao == "6":
                self.controlador_sistema.controlador_pagamento.abrir_tela()

            elif opcao == "7":
                print("Saindo do sistema...")
                break

            else:
                print("Opção inválida!")