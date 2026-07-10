from controller.controlador_clinica import ControladorClinica
from controller.controlador_paciente import ControladorPaciente
from controller.controlador_profissional import ControladorProfissional
from controller.controlador_tipo_atendimento import ControladorTipoAtendimento
from controller.controlador_atendimento import ControladorAtendimento
from controller.controlador_pagamento import ControladorPagamento
from view_gui.tela_sistema_gui import TelaSistemaGUI

class ControladorSistema:

    def __init__(self):
        self.controlador_clinica = ControladorClinica(self)
        self.controlador_paciente = ControladorPaciente(self)
        self.controlador_profissional = ControladorProfissional(self)
        self.controlador_tipo_atendimento = ControladorTipoAtendimento(self)
        self.controlador_atendimento = ControladorAtendimento(self)
        self.controlador_pagamento = ControladorPagamento(self)
        self.tela_sistema_gui = TelaSistemaGUI(self)

    def iniciar_sistema(self):
        self.tela_sistema_gui.abrir_tela()
