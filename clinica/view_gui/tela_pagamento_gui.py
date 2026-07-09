import tkinter as tk
from tkinter import ttk, messagebox

class TelaPagamentoGUI:

    def __init__(self, controlador_sistema):
        self.controlador_sistema = controlador_sistema
        self.janela = None

    def abrir_tela(self):
        self.janela = tk.Tk()
        self.janela.title("Menu Pagamento")
        self.janela.geometry("400x300")

        titulo = tk.Label(
            self.janela,
            text="Gerenciamento de Pagamentos",
            font=("Arial", 14, "bold")
        )
        titulo.pack(pady=20)

        tk.Button(
            self.janela, text="Incluir Pagamento", width=30,
            command=self.abrir_formulario_inclusao
        ).pack(pady=5)

        tk.Button(
            self.janela, text="Listar Pagamentos", width=30,
            command=self.abrir_janela_listagem
        ).pack(pady=5)

        tk.Button(
            self.janela, text="Voltar", width=30,
            command=self.janela.destroy
        ).pack(pady=20)

        self.janela.mainloop()

    def abrir_formulario_inclusao(self):
        atendimentos = self.controlador_sistema.controlador_atendimento.listar_atendimentos()

        if len(atendimentos) == 0:
            messagebox.showinfo("Aviso", "Nenhum atendimento cadastrado para realizar pagamento.")
            return

        janela_form = tk.Toplevel(self.janela)
        janela_form.title("Incluir Pagamento")
        janela_form.geometry("450x550")

        tk.Label(janela_form, text="Selecione o Atendimento:").pack(pady=2)
        opcoes_atendimento = [f"{a.paciente.nome} | {a.data}" for a in atendimentos]
        combo_atendimento = ttk.Combobox(janela_form, values=opcoes_atendimento, width=40, state="readonly")
        combo_atendimento.pack(pady=2)

        tk.Label(janela_form, text="Data do Pagamento (dd/mm/aaaa):").pack(pady=2)
        ent_data = tk.Entry(janela_form, width=43)
        ent_data.pack(pady=2)

        tk.Label(janela_form, text="Valor Pago:").pack(pady=2)
        ent_valor = tk.Entry(janela_form, width=43)
        ent_valor.pack(pady=2)

        tk.Label(janela_form, text="Tipo de Pagamento:").pack(pady=2)
        combo_tipo = ttk.Combobox(janela_form, values=["DINHEIRO", "PIX", "CARTAO"], width=40, state="readonly")
        combo_tipo.pack(pady=2)

        tk.Label(janela_form, text="CPF do Pagador (Preencha apenas se for PIX):").pack(pady=2)
        ent_cpf = tk.Entry(janela_form, width=43)
        ent_cpf.pack(pady=2)

        tk.Label(janela_form, text="Número do Cartão (Preencha apenas se for CARTÃO):").pack(pady=2)
        ent_cartao = tk.Entry(janela_form, width=43)
        ent_cartao.pack(pady=2)

        tk.Label(janela_form, text="Bandeira do Cartão (Preencha apenas se for CARTÃO):").pack(pady=2)
        ent_bandeira = tk.Entry(janela_form, width=43)
        ent_bandeira.pack(pady=2)

        def salvar_dados():
            try:
                if combo_atendimento.current() == -1:
                    raise ValueError("Selecione um atendimento.")
                if not combo_tipo.get():
                    raise ValueError("Selecione um tipo de pagamento.")

                idx_atendimento = combo_atendimento.current()
                atendimento = atendimentos[idx_atendimento]
                paciente = atendimento.paciente

                data = ent_data.get()
                valor_pago = float(ent_valor.get())
                tipo_pagamento = combo_tipo.get()

                cpf = None
                numero_cartao = None
                bandeira = None

                if tipo_pagamento == "PIX":
                    cpf = ent_cpf.get()
                    if not cpf:
                        raise ValueError("O CPF é obrigatório quando o tipo de pagamento é PIX.")
                        
                elif tipo_pagamento == "CARTAO":
                    numero_cartao = ent_cartao.get()
                    bandeira = ent_bandeira.get()
                    if not numero_cartao or not bandeira:
                        raise ValueError("Número do cartão e Bandeira são obrigatórios quando o tipo de pagamento é CARTÃO.")
                    
                self.controlador_sistema.controlador_pagamento.incluir_pagamento(
                    data, atendimento, paciente, valor_pago, tipo_pagamento, cpf, numero_cartao, bandeira
                )
                messagebox.showinfo("Sucesso", "Pagamento registrado com sucesso!")
                janela_form.destroy()

            except ValueError as e:
                messagebox.showerror("Erro de Validação", f"Dados inválidos: {e}")
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

        tk.Button(janela_form, text="Salvar Pagamento", command=salvar_dados, bg="green", fg="white", width=20).pack(pady=20)

    def abrir_janela_listagem(self):
        pagamentos = self.controlador_sistema.controlador_pagamento.listar_pagamentos()

        janela_lista = tk.Toplevel(self.janela)
        janela_lista.title("Listagem de Pagamentos")
        janela_lista.geometry("500x400")

        txt_area = tk.Text(janela_lista, wrap="word", padx=10, pady=10)
        txt_area.pack(expand=True, fill="both")

        if len(pagamentos) == 0:
            txt_area.insert("1.0", "Nenhum pagamento cadastrado.")
        else:
            conteudo = ""
            for p in pagamentos:
                conteudo += f"Data: {p.data}\n"
                conteudo += f"Paciente: {p.paciente.nome}\n"
                conteudo += f"Valor pago: R$ {p.valor_pago:.2f}\n"
                conteudo += f"Detalhes: {p.obter_dados_pagamento()}\n"
                conteudo += "-"*40 + "\n"
            txt_area.insert("1.0", conteudo)

        txt_area.config(state="disabled")