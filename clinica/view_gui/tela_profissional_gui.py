import tkinter as tk
from tkinter import messagebox


class TelaProfissionalGUI:

    def __init__(self, controlador_sistema):
        self.controlador_sistema = controlador_sistema
        self.janela = tk.Tk()
        self.janela.title("Cadastro de Profissionais")

        tk.Label(self.janela, text="Nome").grid(row=0, column=0)
        self.entrada_nome = tk.Entry(self.janela)
        self.entrada_nome.grid(row=0, column=1)

        tk.Label(self.janela, text="Celular").grid(row=1, column=0)
        self.entrada_celular = tk.Entry(self.janela)
        self.entrada_celular.grid(row=1, column=1)

        tk.Label(self.janela, text="CPF").grid(row=2, column=0)
        self.entrada_cpf = tk.Entry(self.janela)
        self.entrada_cpf.grid(row=2, column=1)

        tk.Label(self.janela, text="Especialidade").grid(row=3, column=0)
        self.entrada_especialidade = tk.Entry(self.janela)
        self.entrada_especialidade.grid(row=3, column=1)

        tk.Label(self.janela, text="Registro").grid(row=4, column=0)
        self.entrada_registro = tk.Entry(self.janela)
        self.entrada_registro.grid(row=4, column=1)

        tk.Button(self.janela, text="Incluir", command=self.incluir).grid(row=5, column=0)
        tk.Button(self.janela, text="Listar", command=self.listar).grid(row=5, column=1)
        tk.Button(self.janela, text="Alterar", command=self.alterar).grid(row=6, column=0)
        tk.Button(self.janela, text="Excluir", command=self.excluir).grid(row=6, column=1)

        self.texto_resultado = tk.Text(self.janela, height=10, width=60)
        self.texto_resultado.grid(row=7, column=0, columnspan=2)

    def incluir(self):
        try:
            self.controlador_sistema.controlador_profissional.incluir_profissional(
                self.entrada_especialidade.get(),
                self.entrada_registro.get(),
                self.entrada_nome.get(),
                self.entrada_celular.get(),
                self.entrada_cpf.get()
            )

            messagebox.showinfo("Sucesso", "Profissional cadastrado com sucesso!")
            self.listar()
        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))

    def listar(self):
        self.texto_resultado.delete("1.0", tk.END)
        profissionais = self.controlador_sistema.controlador_profissional.listar_profissionais()

        if not profissionais:
            self.texto_resultado.insert(tk.END, "Nenhum profissional cadastrado.")
            return

        for profissional in profissionais:
            self.texto_resultado.insert(
                tk.END,
                f"Nome: {profissional.nome} | CPF: {profissional.cpf} | Especialidade: {profissional.especialidade} | Registro: {profissional.registro}\n"
            )

    def alterar(self):
        try:
            self.controlador_sistema.controlador_profissional.alterar_profissional(
                self.entrada_registro.get(),
                self.entrada_especialidade.get(),
                self.entrada_nome.get(),
                self.entrada_celular.get()
            )

            messagebox.showinfo("Sucesso", "Profissional alterado com sucesso!")
            self.listar()
        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))

    def excluir(self):
        try:
            self.controlador_sistema.controlador_profissional.excluir_profissional(
                self.entrada_registro.get()
            )

            messagebox.showinfo("Sucesso", "Profissional excluído com sucesso!")
            self.listar()
        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))

    def abrir_tela(self):
        self.janela.mainloop()
