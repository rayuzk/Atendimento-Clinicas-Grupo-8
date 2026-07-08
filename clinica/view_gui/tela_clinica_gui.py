import tkinter as tk
from tkinter import messagebox


class TelaClinicaGUI:

    def __init__(self, controlador_sistema):
        self.controlador_sistema = controlador_sistema
        self.janela = tk.Tk()
        self.janela.title("Cadastro de Clínicas")

        tk.Label(self.janela, text="Nome").grid(row=0, column=0)
        self.entrada_nome = tk.Entry(self.janela)
        self.entrada_nome.grid(row=0, column=1)

        tk.Label(self.janela, text="Cidade").grid(row=1, column=0)
        self.entrada_cidade = tk.Entry(self.janela)
        self.entrada_cidade.grid(row=1, column=1)

        tk.Label(self.janela, text="Descrição").grid(row=2, column=0)
        self.entrada_descricao = tk.Entry(self.janela)
        self.entrada_descricao.grid(row=2, column=1)

        tk.Button(self.janela, text="Incluir", command=self.incluir).grid(row=3, column=0)
        tk.Button(self.janela, text="Listar", command=self.listar).grid(row=3, column=1)
        tk.Button(self.janela, text="Alterar", command=self.alterar).grid(row=4, column=0)
        tk.Button(self.janela, text="Excluir", command=self.excluir).grid(row=4, column=1)

        self.texto_resultado = tk.Text(self.janela, height=10, width=50)
        self.texto_resultado.grid(row=5, column=0, columnspan=2)

    def incluir(self):
        try:
            self.controlador_sistema.controlador_clinica.incluir_clinica(
                self.entrada_nome.get(),
                self.entrada_cidade.get(),
                self.entrada_descricao.get()
            )
            messagebox.showinfo("Sucesso", "Clínica cadastrada com sucesso!")
            self.listar()
        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))

    def listar(self):
        self.texto_resultado.delete("1.0", tk.END)
        clinicas = self.controlador_sistema.controlador_clinica.listar_clinicas()

        if not clinicas:
            self.texto_resultado.insert(tk.END, "Nenhuma clínica cadastrada.")
            return

        for clinica in clinicas:
            self.texto_resultado.insert(
                tk.END,
                f"Nome: {clinica.nome} | Cidade: {clinica.cidade} | Descrição: {clinica.descricao}\n"
            )

    def alterar(self):
        try:
            self.controlador_sistema.controlador_clinica.alterar_clinica(
                self.entrada_nome.get(),
                self.entrada_cidade.get(),
                self.entrada_descricao.get()
            )
            messagebox.showinfo("Sucesso", "Clínica alterada com sucesso!")
            self.listar()
        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))

    def excluir(self):
        try:
            self.controlador_sistema.controlador_clinica.excluir_clinica(
                self.entrada_nome.get()
            )
            messagebox.showinfo("Sucesso", "Clínica excluída com sucesso!")
            self.listar()
        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))

    def abrir_tela(self):
          self.janela.mainloop()
