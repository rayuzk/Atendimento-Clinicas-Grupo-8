from model.atendimento import Atendimento

class ControladorAtendimento:
    def __init__(self):
        self.atendimentos = []

    def incluir_atendimento(
        self,
        clinica,
        paciente,
        profissional,
        data,
        horario_inicio,
        horario_fim,
        tipo_atendimento,
        valor
    ): 
        
        if clinica is None:
            print("Erro: clínica inválida")
            return

        if paciente is None:
            print("Erro: paciente inválido")
            return

        if profissional is None:
            print("Erro: profissional inválido")
            return

        if data is None:
            print("Erro: data inválida")
            return
        
        if horario_inicio is None:
            print("Erro: horario de início inválido")
            return
        
        if horario_fim is None:
            print("Erro: horário fim inválido")
            return

        if tipo_atendimento is None:
            print("Erro: tipo de atendimento inválido")
            return
        
        if horario_inicio >= horario_fim:
          print("O horário de ínicio deve ser antes do fim")
          return
        
        if valor < 0:
          print("Valor não pode ser negativo")
          return
        
        atendimento = Atendimento(
        clinica,
        paciente,
        profissional,
        data,
        horario_inicio,
        horario_fim,
        tipo_atendimento,
        valor
        )

        self.atendimentos.append(atendimento)

    def listar_atendimentos(self):
        return self.atendimentos
    
    def excluir_atendimento(self, atendimento):
        if atendimento in self.atendimentos:
            self.atendimentos.remove(atendimento)

    def adicionar_procedimento(self, atendimento, procedimento):
        if atendimento is None:
            print("Atendimento inválido")
            return
        atendimento.adicionar_procedimento(procedimento)
        print("Procedimento adicionado")

    def adicionar_pagamento(self, atendimento, pagamento):
        
        if atendimento is None:
            print("Atendimento inválido")
            return
        
        if pagamento is None:
            print("Pagamento inválido")
            return

        if pagamento.valor_pago < atendimento.valor:
            print("Erro: o valor do atendimento é maior que o valor pago")
            return
        
        atendimento.adicionar_pagamento(pagamento)
        print("Pagamento registrado")

    def busca_paciente(self, paciente):
        busca = []

        for a in self.atendimentos:
            if a.paciente == paciente:
                busca.append(a)
        
        return busca


    def busca_clinica(self, clinica):
        busca = []

        for a in self.atendimentos:
            if a.clinica == clinica:
                busca.append(a)
        
        return busca

    def busca_profissional(self, profissional):
        busca = []

        for a in self.atendimentos:
            if a.profissional == profissional:
                busca.append(a)
        
        return busca

    
    def relatorio_procedimentos_mais_realizados(self):
        contagem = {}

        for atendimento in self.atendimentos:
            for procedimento in atendimento.procedimentos:

                descricao = procedimento.descricao

                if descricao in contagem:
                    contagem[descricao] = contagem[descricao] + 1
                else:
                    contagem[descricao] = 1

        if len(contagem) == 0:
            print("Nenhum procedimento registrado.")
            return

        print("\nRelatórios de procedimentos mais realizados:")

        for descricao in contagem:
            print(descricao, "->", contagem[descricao], "vezes")

    
    def relatorio_procedimentos_valor(self):
        todos_procedimentos = []

        for atendimento in self.atendimentos:
            for procedimento in atendimento.procedimentos:
                todos_procedimentos.append(procedimento)

        if len(todos_procedimentos) == 0:
            print("Nenhum procedimento registrado.")
            return

        mais_caro = todos_procedimentos[0]
        mais_barato = todos_procedimentos[0]

        for procedimento in todos_procedimentos:

            if procedimento.custo > mais_caro.custo:
                mais_caro = procedimento

            if procedimento.custo < mais_barato.custo:
                mais_barato = procedimento

        print("\nRelatório de procedimentos mais caros e mais baratos:")
        print("Mais caro:", mais_caro.descricao, "- R$", mais_caro.custo)
        print("Mais barato:", mais_barato.descricao, "- R$", mais_barato.custo)

    
    def abrir_tela(self):
        pass