class TelaAtendimento:
    
    def entra_dados(self):
        clinica = input("Digite a clinica: ")
        paciente = input("Digite o nome do paciente: ")
        profissional = input("Digite o nome do profissional: ")
        data = input("Digite a data: ")
        horario_inicio = input("Digite o horário de início: ")
        horario_fim = input("Digite o horário fim: ")
        tipo_atendimento = input("Digite o tipo de atendimento: ")
        valor = float(input("Digite o valor: "))

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

    def mostrar_atendimentos(self):
        
        atendimentos = self.controlador_sistema.controlador_atendimento.listar_atendimentos()
        
        if len(atendimentos) == 0:
            print("Nenhum atendimento cadastrado até o momento")
            return
        
        for atendimento in atendimentos:
            print("Clínica:", atendimento.clinica)
            print("Paciente:", atendimento.paciente)
            print("Profissional:", atendimento.profissional)
            print("Data:", atendimento.data)
            print("Horário início:", atendimento.horario_inicio)
            print("Horário fim:", atendimento.horario_fim)
            print("Tipo:", atendimento.tipo_atendimento)
            print("Valor:", atendimento.valor)

    def abrir_tela(self):

        while True:
            print("\nMenu Atendimento")
            print("(1) Incluir atendimento")
            print("(2) Listar atendimentos")
            print("(3) Excluir atendimento")
            print("(4) Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
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

            elif opcao == "2":
                self.mostrar_atendimentos()

            
            elif opcao == "3":
                atendimentos = self.controlador_sistema.controlador_atendimento.listar_atendimentos()

                if len(atendimentos) == 0:
                    print("Nenhum atendimento para excluir.")
                else:
                    for i in range(len(atendimentos)):
                        atendimento = atendimentos[i]
                    print(i, "-", atendimento.paciente, "|", atendimento.data)

                    indice = int(input("Digite o índice para excluir: "))

                    if 0 <= indice < len(atendimentos):
                        self.controlador_sistema.controlador_atendimento.excluir_atendimento(atendimentos[indice])
                        print("Atendimento excluído")
                    else:
                        print("Índice inválido.")

            
            elif opcao == "4":
                break

            else:
                print("Opção inválida!")
