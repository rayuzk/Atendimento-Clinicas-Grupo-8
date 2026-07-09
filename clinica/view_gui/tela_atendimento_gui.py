import tkinter as tk
from tkinter import ttk, messagebox

class TelaAtendimento:

    def __init__(self, controlador_sistema):
        self.controlador_sistema = controlador_sistema
        self.janela = None

    def abrir_tela(self):
        self.janela = tk.Tk()
        self.janela.title("Menu Atendimento")
        self.janela.geometry("400x400")

        titulo = tk.Label(
            self.janela,
            text="Gerenciamento de Atendimentos",
            font=("Arial", 14, "bold")
        )
        titulo.pack(pady=20)

        tk.Button(
            self.janela, text="Incluir Atendimento", width=30,
            command=self.abrir_formulario_inclusao
        ).pack(pady=5)

        tk.Button(
            self.janela, text="Listar Atendimentos", width=30,
            command=self.abrir_janela_listagem
        ).pack(pady=5)

        tk.Button(
            self.janela, text="Excluir Atendimento", width=30,
            command=self.abrir_janela_exclusao
        ).pack(pady=5)

        tk.Button(
            self.janela, text="Relatórios", width=30,
            command=self.abrir_tela_relatorios
        ).pack(pady=5)

        tk.Button(
            self.janela, text="Voltar", width=30,
            command=self.janela.destroy
        ).pack(pady=20)

        self.janela.mainloop()

    def abrir_formulario_inclusao(self):
        janela_form = tk.Toplevel(self.janela)
        janela_form.title("Incluir Atendimento")
        janela_form.geometry("450x520")

        clinicas = self.controlador_sistema.controlador_clinica.listar_clinicas()
        pacientes = self.controlador_sistema.controlador_paciente.listar_pacientes()
        profissionais = self.controlador_sistema.controlador_profissional.listar_profissionais()
        tipos = self.controlador_sistema.controlador_tipo_atendimento.listar_tipos_atendimento()

        tk.Label(janela_form, text="Clínica:").pack(pady=2)
        combo_clinica = ttk.Combobox(janela_form, values=[c.nome for c in clinicas], width=35, state="readonly")
        combo_clinica.pack(pady=2)

        tk.Label(janela_form, text="Paciente:").pack(pady=2)
        combo_paciente = ttk.Combobox(janela_form, values=[p.nome for p in pacientes], width=35, state="readonly")
        combo_paciente.pack(pady=2)

        tk.Label(janela_form, text="Profissional:").pack(pady=2)
        combo_profissional = ttk.Combobox(janela_form, values=[pr.nome for pr in profissionais], width=35, state="readonly")
        combo_profissional.pack(pady=2)

        tk.Label(janela_form, text="Tipo de Atendimento:").pack(pady=2)
        combo_tipo = ttk.Combobox(janela_form, values=[t.descricao for t in tipos], width=35, state="readonly")
        combo_tipo.pack(pady=2)

        tk.Label(janela_form, text="Data (dd/mm/aaaa):").pack(pady=2)
        ent_data = tk.Entry(janela_form, width=38)
        ent_data.pack(pady=2)

        tk.Label(janela_form, text="Horário Início (HH:MM):").pack(pady=2)
        ent_ini = tk.Entry(janela_form, width=38)
        ent_ini.pack(pady=2)

        tk.Label(janela_form, text="Horário Fim (HH:MM):").pack(pady=2)
        ent_fim = tk.Entry(janela_form, width=38)
        ent_fim.pack(pady=2)

        tk.Label(janela_form, text="Valor:").pack(pady=2)
        ent_valor = tk.Entry(janela_form, width=38)
        ent_valor.pack(pady=2)

        def salvar_dados():
            try:
                if not (combo_clinica.get() and combo_paciente.get() and combo_profissional.get() and combo_tipo.get()):
                    raise ValueError("Por favor, selecione todas as opções das listas.")

                clinica = clinicas[combo_clinica.current()]
                paciente = pacientes[combo_paciente.current()]
                profissional = profissionais[combo_profissional.current()]
                tipo_atendimento = tipos[combo_tipo.current()]

                self.controlador_sistema.controlador_atendimento.incluir_atendimento(
                    clinica, paciente, profissional,
                    ent_data.get(), ent_ini.get(), ent_fim.get(),
                    tipo_atendimento, float(ent_valor.get())
                )
                messagebox.showinfo("Sucesso", "Atendimento cadastrado com sucesso!")
                janela_form.destroy()
            except ValueError as e:
                messagebox.showerror("Erro de Validação", f"Dados inválidos: {e}")
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

        tk.Button(janela_form, text="Salvar Atendimento", command=salvar_dados, bg="green", fg="white", width=20).pack(pady=15)

    def abrir_janela_listagem(self):
        atendimentos = self.controlador_sistema.controlador_atendimento.listar_atendimentos()
        
        janela_lista = tk.Toplevel(self.janela)
        janela_lista.title("Listagem de Atendimentos")
        janela_lista.geometry("500x400")

        txt_area = tk.Text(janela_lista, wrap="word", padx=10, pady=10)
        txt_area.pack(expand=True, fill="both")

        if len(atendimentos) == 0:
            txt_area.insert("1.0", "Nenhum atendimento cadastrado.")
        else:
            conteudo = ""
            for a in atendimentos:
                conteudo += f"Clínica: {a.clinica.nome}\n"
                conteudo += f"Paciente: {a.paciente.nome}\n"
                conteudo += f"Profissional: {a.profissional.nome}\n"
                conteudo += f"Data: {a.data} | Início: {a.horario_inicio} | Fim: {a.horario_fim}\n"
                conteudo += f"Tipo: {a.tipo_atendimento.descricao}\n"
                conteudo += f"Valor: R$ {a.valor:.2f}\n"
                conteudo += "-"*40 + "\n"
            txt_area.insert("1.0", conteudo)
        
        txt_area.config(state="disabled")

    def abrir_janela_exclusao(self):
        atendimentos = self.controlador_sistema.controlador_atendimento.listar_atendimentos()

        if len(atendimentos) == 0:
            messagebox.showinfo("Aviso", "Nenhum atendimento para excluir.")
            return

        janela_exc = tk.Toplevel(self.janela)
        janela_exc.title("Excluir Atendimento")
        janela_exc.geometry("400x250")

        tk.Label(janela_exc, text="Selecione o atendimento que deseja remover:", font=("Arial", 10, "bold")).pack(pady=10)
        
        opcoes = [f"{a.paciente.nome} | {a.data} | {a.clinica.nome}" for a in atendimentos]
        combo_exc = ttk.Combobox(janela_exc, values=opcoes, width=45, state="readonly")
        combo_exc.pack(pady=10)

        def confirmar_exclusao():
            idx = combo_exc.current()
            if idx >= 0:
                if messagebox.askyesno("Confirmar", "Tem certeza que deseja excluir este atendimento?"):
                    self.controlador_sistema.controlador_atendimento.excluir_atendimento(atendimentos[idx])
                    messagebox.showinfo("Sucesso", "Atendimento excluído com sucesso!")
                    janela_exc.destroy()
            else:
                messagebox.showwarning("Aviso", "Selecione um atendimento para excluir.")

        tk.Button(janela_exc, text="Excluir", command=confirmar_exclusao, bg="red", fg="white", width=15).pack(pady=15)

    def abrir_tela_relatorios(self):
        janela_rel = tk.Toplevel(self.janela)
        janela_rel.title("Relatórios do Sistema")
        janela_rel.geometry("400x350")

        tk.Label(janela_rel, text="Selecione o Relatório Desejado:", font=("Arial", 12, "bold")).pack(pady=15)

        def exibir_resultado(titulo, texto):
            janela_res = tk.Toplevel(janela_rel)
            janela_res.title(titulo)
            tk.Label(janela_res, text=texto, justify="left", font=("Courier", 10), padx=15, pady=15).pack()


        def rel_clinicas():
            resultado = self.controlador_sistema.controlador_atendimento.clinicas_com_mais_atendimentos()
            if len(resultado) == 0:
                return messagebox.showinfo("Relatório", "Nenhum dado encontrado.")
            
            txt = ""
            for nome, qtd in resultado.items():
                txt += f"{nome} -> {qtd} atendimento(s)\n"
                
            exibir_resultado("Clínicas com mais Atendimentos", txt)

        def rel_valores():
            caro = self.controlador_sistema.controlador_atendimento.atendimento_mais_caro()
            barato = self.controlador_sistema.controlador_atendimento.atendimento_mais_barato()
            if caro is None: 
                return messagebox.showinfo("Relatório", "Nenhum dado encontrado.")
            
            txt = f"Mais caro:\n{caro.paciente.nome} | R$ {caro.valor:.2f}\n\nMais barato:\n{barato.paciente.nome} | R$ {barato.valor:.2f}"
            exibir_resultado("Atendimentos: Limites de Valores", txt)

        def rel_procedimentos_qtd():
            resultado = self.controlador_sistema.controlador_atendimento.relatorio_procedimentos_mais_realizados()
            if len(resultado) == 0:
                return messagebox.showinfo("Relatório", "Nenhum dado encontrado.")
            
            txt = ""
            for descricao, qtd in resultado.items():
                txt += f"{descricao} -> {qtd} vez(es)\n"
                
            exibir_resultado("Procedimentos Mais Realizados", txt)

        def rel_procedimentos_val():
            caro, barato = self.controlador_sistema.controlador_atendimento.relatorio_procedimentos_valor()
            if caro is None:
                return messagebox.showinfo("Relatório", "Nenhum dado encontrado.")
            
            txt = f"Procedimento Mais Caro:\n{caro.tipo_atendimento.descricao} - R$ {caro.valor:.2f}\n\nProcedimento Mais Barato:\n{barato.tipo_atendimento.descricao} - R$ {barato.valor:.2f}"
            exibir_resultado("Valores de Procedimentos", txt)

        tk.Button(janela_rel, text="Clínicas com mais atendimentos", width=35, command=rel_clinicas).pack(pady=5)
        tk.Button(janela_rel, text="Atendimento mais caro e mais barato", width=35, command=rel_valores).pack(pady=5)
        tk.Button(janela_rel, text="Procedimentos mais realizados", width=35, command=rel_procedimentos_qtd).pack(pady=5)
        tk.Button(janela_rel, text="Procedimentos mais caros/baratos", width=35, command=rel_procedimentos_val).pack(pady=5)
        tk.Button(janela_rel, text="Voltar", width=35, command=janela_rel.destroy).pack(pady=15)