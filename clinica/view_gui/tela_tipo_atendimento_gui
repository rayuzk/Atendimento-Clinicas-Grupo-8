import tkinter as tk
from tkinter import messagebox


class TelaTipoAtendimentoGUI:

    def __init__(self, controlador_sistema):
        self.controlador_sistema = controlador_sistema
        self.janela = tk.Tk()
        self.janela.title("Cadastro de Tipos de Atendimento")

        tk.Label(self.janela, text="Descrição").grid(row=0, column=0)
        self.entrada_descricao = tk.Entry(self.janela)
        self.entrada_descricao.grid(row=0, column=1)

        tk.Button(self.janela, text="Incluir", command=self.incluir).grid(row=1, column=0)
        tk.Button(self.janela, text="Listar", command=self.listar).grid(row=1, column=1)
        tk.Button(self.janela, text="Alterar", command=self.alterar).grid(row=2, column=0)
        tk.Button(self.janela, text="Excluir", command=self.excluir).grid(row=2, column=1)

        self.texto_resultado = tk.Text(self.janela, height=10, width=50)
        self.texto_resultado.grid(row=3, column=0, columnspan=2)

    def incluir(self):
        try:
            self.controlador_sistema.controlador_tipo_atendimento.incluir_tipo_atendimento(
                self.entrada_descricao.get()
            )

            messagebox.showinfo("Sucesso", "Tipo de atendimento cadastrado com sucesso!")
            self.listar()
        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))

    def listar(self):
        self.texto_resultado.delete("1.0", tk.END)
        tipos = self.controlador_sistema.controlador_tipo_atendimento.listar_tipos_atendimento()

        if not tipos:
            self.texto_resultado.insert(tk.END, "Nenhum tipo de atendimento cadastrado.")
            return

        for tipo in tipos:
            self.texto_resultado.insert(
                tk.END,
                f"Descrição: {tipo.descricao}\n"
            )

    def alterar(self):
        try:
            nova_descricao = self.entrada_descricao.get()

            self.controlador_sistema.controlador_tipo_atendimento.alterar_tipo_atendimento(
                self.entrada_descricao.get(),
                nova_descricao
            )

            messagebox.showinfo("Sucesso", "Tipo de atendimento alterado com sucesso!")
            self.listar()
        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))

    def excluir(self):
        try:
            self.controlador_sistema.controlador_tipo_atendimento.excluir_tipo_atendimento(
                self.entrada_descricao.get()
            )

            messagebox.showinfo("Sucesso", "Tipo de atendimento excluído com sucesso!")
            self.listar()
        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))

    def abrir_tela(self):
        self.janela.mainloop()
