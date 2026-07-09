'''
class TelaAtendimento:

    def __init__(self, controlador_sistema):
        self.controlador_sistema = controlador_sistema

    def entra_dados(self):
        print("\nClínicas disponíveis:")
        clinicas = self.controlador_sistema.controlador_clinica.listar_clinicas()
        
        for i in range(len(clinicas)):
            print(i, "-", clinicas[i].nome)
        indice_clinica = int(input("Escolha o índice da clínica: "))
        clinica = clinicas[indice_clinica]

        print("\nPacientes disponíveis:")
        pacientes = self.controlador_sistema.controlador_paciente.listar_pacientes()
        for i in range(len(pacientes)):
            print(i, "-", pacientes[i].nome)
        indice_paciente = int(input("Escolha o índice do paciente: "))
        paciente = pacientes[indice_paciente]

        print("\nProfissionais disponíveis:")
        profissionais = self.controlador_sistema.controlador_profissional.listar_profissionais()
        
        for i in range(len(profissionais)):
            print(i, "-", profissionais[i].nome)
        indice_profissional = int(input("Escolha o índice do profissional: "))
        profissional = profissionais[indice_profissional]

        print("\nTipos de atendimento disponíveis:")
        tipos = self.controlador_sistema.controlador_tipo_atendimento.listar_tipos_atendimento()
        for i in range(len(tipos)):
            print(i, "-", tipos[i].descricao)
        indice_tipo = int(input("Escolha o índice do tipo de atendimento: "))
        tipo_atendimento = tipos[indice_tipo]

        data = input("Data (dd/mm/aaaa): ")
        horario_inicio = input("Horário de início (HH:MM): ")
        horario_fim = input("Horário fim (HH:MM): ")
        valor = float(input("Valor: "))

        return {
            "clinica": clinica,
            "paciente": paciente,
            "profissional": profissional,
            "data": data,
            "horario_inicio": horario_inicio,
            "horario_fim": horario_fim,
            "tipo_atendimento": tipo_atendimento,
            "valor": valor
        }

    def mostrar_atendimentos(self, atendimentos):
        if len(atendimentos) == 0:
            print("Nenhum atendimento cadastrado.")
            return
        for atendimento in atendimentos:
            print("Clínica:", atendimento.clinica.nome)
            print("Paciente:", atendimento.paciente.nome)
            print("Profissional:", atendimento.profissional.nome)
            print("Data:", atendimento.data)
            print("Horário início:", atendimento.horario_inicio)
            print("Horário fim:", atendimento.horario_fim)
            print("Tipo:", atendimento.tipo_atendimento.descricao)
            print("Valor: R$", atendimento.valor)
            print("---")

    def abrir_tela(self):
        while True:
            print("\nMenu Atendimento")
            print("(1) Incluir atendimento")
            print("(2) Listar atendimentos")
            print("(3) Excluir atendimento")
            print("(4) Relatórios")
            print("(5) Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                try:
                    dados = self.entra_dados()
                    self.controlador_sistema.controlador_atendimento.incluir_atendimento(
                        dados["clinica"],
                        dados["paciente"],
                        dados["profissional"],
                        dados["data"],
                        dados["horario_inicio"],
                        dados["horario_fim"],
                        dados["tipo_atendimento"],
                        dados["valor"]
                    )
                    print("Atendimento cadastrado com sucesso!")
                except ValueError as e:
                    print("Erro:", e)

            elif opcao == "2":
                atendimentos = self.controlador_sistema.controlador_atendimento.listar_atendimentos()
                self.mostrar_atendimentos(atendimentos)

            elif opcao == "3":
                atendimentos = self.controlador_sistema.controlador_atendimento.listar_atendimentos()

                if len(atendimentos) == 0:
                    print("Nenhum atendimento para excluir.")
                else:
                    for i in range(len(atendimentos)):   
                        print(i, "-", atendimentos[i].paciente.nome, "|", atendimentos[i].data)

                    try:
                        indice = int(input("Digite o índice para excluir: "))
                        if 0 <= indice < len(atendimentos):
                            self.controlador_sistema.controlador_atendimento.excluir_atendimento(
                                atendimentos[indice]
                            )
                            print("Atendimento excluído.")
                        else:
                            print("Índice inválido.")
                    except ValueError as e:
                        print("Erro:", e)

            elif opcao == "4":
                self.abrir_tela_relatorios()

            elif opcao == "5":
                break

            else:
                print("Opção inválida!")

    def abrir_tela_relatorios(self):
        while True:
            print("\nRelatórios")
            print("(1) Clínicas com mais atendimentos")
            print("(2) Atendimento mais caro e mais barato")
            print("(3) Procedimentos mais realizados")
            print("(4) Procedimentos mais caros e mais baratos")
            print("(5) Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                resultado = self.controlador_sistema.controlador_atendimento.clinicas_com_mais_atendimentos()
                if len(resultado) == 0:
                    print("Nenhum atendimento registrado.")
                else:
                    print("\nClínicas com mais atendimentos:")
                    for nome in resultado:
                        print(nome, "->", resultado[nome], "atendimento(s)")

            elif opcao == "2":
                mais_caro = self.controlador_sistema.controlador_atendimento.atendimento_mais_caro()
                mais_barato = self.controlador_sistema.controlador_atendimento.atendimento_mais_barato()
                if mais_caro is None:
                    print("Nenhum atendimento registrado.")
                else:
                    print("\nAtendimento mais caro:")
                    print(mais_caro.paciente.nome, "| R$", mais_caro.valor)
                    print("Atendimento mais barato:")
                    print(mais_barato.paciente.nome, "| R$", mais_barato.valor)

            elif opcao == "3":
                resultado = self.controlador_sistema.controlador_atendimento.relatorio_procedimentos_mais_realizados()
                if len(resultado) == 0:
                    print("Nenhum procedimento registrado.")
                else:
                    print("\nProcedimentos mais realizados:")
                    for descricao in resultado:
                        print(descricao, "->", resultado[descricao], "vez(es)")

            elif opcao == "4":
                mais_caro, mais_barato = self.controlador_sistema.controlador_atendimento.relatorio_procedimentos_valor()
                if mais_caro is None:
                    print("Nenhum procedimento registrado.")
                else:
                    print("\nProcedimento mais caro:", mais_caro.tipo_atendimento.descricao, "- R$", mais_caro.valor)
                    print("Procedimento mais barato:", mais_barato.tipo_atendimento.descricao, "- R$", mais_barato.valor)

            elif opcao == "5":
                break

            else:
                print("Opção inválida!")
'''