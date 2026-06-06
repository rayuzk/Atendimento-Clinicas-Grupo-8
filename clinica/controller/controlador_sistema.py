from controller.controlador_clinica import ControladorClinica
from controller.controlador_paciente import ControladorPaciente
from controller.controlador_profissional import ControladorProfissional
from controller.controlador_tipo_atendimento import ControladorTipoAtendimento
from controller.controlador_atendimento import ControladorAtendimento
from controller.controlador_pagamento import ControladorPagamento

class ControladorSistema:
    def __init__(self):
        self.__controlador_clinica = ControladorClinica(self)
        self.__controlador_paciente = ControladorPaciente(self)
        self.__controlador_profissional = ControladorProfissional(self)
        self.__controlador_tipo_atendimento = ControladorTipoAtendimento(self)
        self.__controlador_atendimento = ControladorAtendimento(self)
        self.__controlador_pagamento = ControladorPagamento(self)

    def iniciar_sistema(self):
        self.abrir_menu()

    def abrir_menu(self):
        while True:
            print("Bem-vindo ao menu principal, selecione a opação desejada :)")
            print("(1) Clínicas")
            print("(2) Pacientes")
            print("(3) Profissionais")
            print("(4) Tipo de atendimento")
            print("(5) Atendimentos")
            print("(6) Pagamentos") 
            print("(7) Sair")

            opcao = input("Minha escolha é a opção: ")

            if opcao == "1":
                self.__controlador_clinica.abrir_tela()
            
            elif opcao == "2":
                self.__controlador_paciente.abrir_tela()

            elif opcao == "3":
                self.__controlador_profissional.abrir_tela()
            
            elif opcao == "4":
                self.__controlador_tipo_atendimento.abrir_tela()
            
            elif opcao == "5":
                self.__controlador_atendimento.abrir_tela()
            
            elif opcao == "6":
                self.__controlador_pagamento.abrir_tela()
            
            elif opcao == "7":
                break
