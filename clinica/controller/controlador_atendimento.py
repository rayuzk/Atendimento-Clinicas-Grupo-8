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
            if a.profissionl == profissional:
                busca.append(a)
        
        return busca


    def abrir_tela(self):
        pass