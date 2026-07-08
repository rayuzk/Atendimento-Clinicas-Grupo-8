import tkinter as tk
from tkinter import messagebox


class TelaPacienteGUI:

    def __init__(self, controlador_sistema):
        self.controlador_sistema = controlador_sistema
        self.janela = tk.Tk()
        self.janela.title("Cadastro de Pacientes")

        tk.Label(self.janela, text="Nome").grid(row=0, column=0)
        self.entrada_nome = tk.Entry(self.janela)
        self.entrada_nome.grid(row=0, column=1)

        tk.Label(self.janela, text="Celular").grid(row=1, column=0)
        self.entrada_celular = tk.Entry(self.janela)
        self.entrada_celular.grid(row=1, column=1)

        tk.Label(self.janela, text="CPF").grid(row=2, column=0)
        self.entrada_cpf = tk.Entry(self.janela)
        self.entrada_cpf.grid(row=2, column=1)

        tk.Label(self.janela, text="Idade").grid(row=3, column=0)
        self.entrada_idade = tk.Entry(self.janela)
        self.entrada_idade.grid(row=3, column=1)

        tk.Button(self.janela, text="Incluir", command=self.incluir).grid(row=4, column=0)
        tk.Button(self.janela, text="Listar", command=self.listar).grid(row=4, column=1)
        tk.Button(self.janela, text="Alterar", command=self.alterar).grid(row=5, column=0)
        tk.Button(self.janela, text="Excluir", command=self.excluir).grid(row=5, column=1)

        self.texto_resultado = tk.Text(self.janela, height=10, width=55)
        self.texto_resultado.grid(row=6, column=0, columnspan=2)

    def incluir(self):
        try:
            idade = int(self.entrada_idade.get())

            self.controlador_sistema.controlador_paciente.incluir_paciente(
                idade,
                self.entrada_nome.get(),
                self.entrada_celular.get(),
                self.entrada_cpf.get()
            )

            messagebox.showinfo("Sucesso", "Paciente cadastrado com sucesso!")
            self.listar()
        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))

    def listar(self):
        self.texto_resultado.delete("1.0", tk.END)
        pacientes = self.controlador_sistema.controlador_paciente.listar_pacientes()

        if not pacientes:
            self.texto_resultado.insert(tk.END, "Nenhum paciente cadastrado.")
            return

        for paciente in pacientes:
            self.texto_resultado.insert(
                tk.END,
                f"Nome: {paciente.nome} | CPF: {paciente.cpf} | Celular: {paciente.celular} | Idade: {paciente.idade}\n"
            )

    def alterar(self):
        try:
            nova_idade = int(self.entrada_idade.get())

            self.controlador_sistema.controlador_paciente.alterar_paciente(
                self.entrada_cpf.get(),
                self.entrada_nome.get(),
                self.entrada_celular.get(),
                nova_idade
            )

            messagebox.showinfo("Sucesso", "Paciente alterado com sucesso!")
            self.listar()
        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))

    def excluir(self):
        try:
            self.controlador_sistema.controlador_paciente.excluir_paciente(
                self.entrada_cpf.get()
            )

            messagebox.showinfo("Sucesso", "Paciente excluído com sucesso!")
            self.listar()
        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))

    def abrir_tela(self):
        self.janela.mainloop()
