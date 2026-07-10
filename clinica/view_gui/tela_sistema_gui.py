import tkinter as tk
from tkinter import messagebox
from view_gui.tela_clinica_gui import TelaClinicaGUI
from view_gui.tela_paciente_gui import TelaPacienteGUI
from view_gui.tela_profissional_gui import TelaProfissionalGUI
from view_gui.tela_tipo_atendimento_gui import TelaTipoAtendimentoGUI
from view_gui.tela_atendimento_gui import TelaAtendimentoGUI
from view_gui.tela_pagamento_gui import TelaPagamentoGUI

class TelaSistemaGUI:

    def __init__(self, controlador_sistema):
        self.controlador_sistema = controlador_sistema
        self.tela_clinica = TelaClinicaGUI(controlador_sistema)
        self.tela_paciente = TelaPacienteGUI(controlador_sistema)
        self.tela_profissional = TelaProfissionalGUI(controlador_sistema)
        self.tela_tipo_atendimento = TelaTipoAtendimentoGUI(controlador_sistema)
        self.tela_atendimento = TelaAtendimentoGUI(controlador_sistema)
        self.tela_pagamento = TelaPagamentoGUI(controlador_sistema)

    def abrir_tela_clinica(self):
        self.tela_clinica.abrir_tela()

    def abrir_tela_paciente(self):
        self.tela_paciente.abrir_tela()

    def abrir_tela_profissional(self):
        self.tela_profissional.abrir_tela()

    def abrir_tela_tipo_atendimento(self):
        self.tela_tipo_atendimento.abrir_tela()

    def abrir_tela_atendimento(self):
        self.tela_atendimento.abrir_tela()

    def abrir_tela_pagamento(self):
        self.tela_pagamento.abrir_tela()

    def abrir_tela(self):
        self.janela = tk.Tk()
        self.janela.title("Sistema de Clínicas")
        self.janela.geometry("400x450")

        titulo = tk.Label(
            self.janela,
            text="Sistema de Clínicas",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=20)

        mensagem = tk.Label(
            self.janela,
            text="Selecione uma opção:"
        )
        mensagem.pack(pady=10)

        tk.Button(
            self.janela,
            text="Clínicas",
            width=30,
            command=self.abrir_tela_clinica
        ).pack(pady=5)

        tk.Button(
            self.janela,
            text="Pacientes",
            width=30,
            command=self.abrir_tela_paciente
        ).pack(pady=5)

        tk.Button(
            self.janela,
            text="Profissionais",
            width=30,
            command=self.abrir_tela_profissional
        ).pack(pady=5)

        tk.Button(
            self.janela,
            text="Tipos de Atendimento",
            width=30,
            command=self.abrir_tela_tipo_atendimento
        ).pack(pady=5)

        tk.Button(
            self.janela,
            text="Atendimentos",
            width=30,
            command=self.abrir_tela_atendimento
        ).pack(pady=5)

        tk.Button(
            self.janela,
            text="Pagamentos",
            width=30,
            command=self.abrir_tela_pagamento
        ).pack(pady=5)

        tk.Button(
            self.janela,
            text="Sair",
            width=30,
            command=self.janela.destroy
        ).pack(pady=20)
        
        self.janela.mainloop()