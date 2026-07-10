from model.atendimento import Atendimento
from dao.atendimento_dao import AtendimentoDAO


class ControladorAtendimento:

    def __init__(self, controlador_sistema):
        self.controlador_sistema = controlador_sistema
        self.__atendimento_dao = AtendimentoDAO()
        self.atendimentos = self.__atendimento_dao.carregar()

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
            raise ValueError("Clínica inválida.")

        if paciente is None:
            raise ValueError("Paciente inválido.")

        if profissional is None:
            raise ValueError("Profissional inválido.")

        if data is None:
            raise ValueError("Data inválida.")

        if horario_inicio is None:
            raise ValueError("Horário de início inválido.")

        if horario_fim is None:
            raise ValueError("Horário fim inválido.")

        if tipo_atendimento is None:
            raise ValueError("Tipo de atendimento inválido.")

        # if horario_inicio >= horario_inicio:
           # raise ValueError("O horário de início deve ser antes do fim.")

        if valor < 0:
            raise ValueError("Valor não pode ser negativo.")

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
        self.__atendimento_dao.salvar(self.atendimentos)
        return atendimento

    def listar_atendimentos(self):
        self.atendimentos = self.__atendimento_dao.carregar()
        return self.atendimentos

    def excluir_atendimento(self, atendimento):
        if atendimento in self.atendimentos:
            self.atendimentos.remove(atendimento)
            self.__atendimento_dao.salvar(self.atendimentos)
        else:
            raise ValueError("Atendimento não encontrado.")

    def adicionar_procedimento(self, atendimento, procedimento):
        if atendimento is None:
            raise ValueError("Atendimento inválido.")
        if procedimento is None:
            raise ValueError("Procedimento inválido.")
        atendimento.adicionar_procedimento(procedimento)
    
        self.__atendimento_dao.salvar(self.atendimentos)

    def adicionar_pagamento(self, atendimento, pagamento):
        if atendimento is None:
            raise ValueError("Atendimento inválido.")
        if pagamento is None:
            raise ValueError("Pagamento inválido.")
        atendimento.adicionar_pagamento(pagamento)
        
        self.__atendimento_dao.salvar(self.atendimentos)

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

    def clinicas_com_mais_atendimentos(self):
        quantidade_por_clinica = {}

        for atendimento in self.atendimentos:
            nome_clinica = atendimento.clinica.nome

            if nome_clinica in quantidade_por_clinica:
                quantidade_por_clinica[nome_clinica] += 1
            else:
                quantidade_por_clinica[nome_clinica] = 1

        return quantidade_por_clinica

    def atendimento_mais_caro(self):
        if not self.atendimentos:
            return None

        return max(
            self.atendimentos,
            key=lambda atendimento: atendimento.valor
        )

    def atendimento_mais_barato(self):
        if not self.atendimentos:
            return None

        return min(
            self.atendimentos,
            key=lambda atendimento: atendimento.valor
        )

    def relatorio_procedimentos_mais_realizados(self):
        contagem = {}

        for atendimento in self.atendimentos:
            descricao = atendimento.tipo_atendimento.descricao                

            if descricao in contagem:
                    contagem[descricao] = contagem[descricao] + 1
            else:
                    contagem[descricao] = 1

        return contagem

    def relatorio_procedimentos_valor(self):
        if len(self.atendimentos) == 0:
            return None, None

        mais_caro = self.atendimentos[0]
        mais_barato = self.atendimentos[0]

        for atendimento in self.atendimentos:
            if atendimento.valor > mais_caro.valor:
                mais_caro = atendimento

            if atendimento.valor < mais_barato.valor:
                mais_barato = atendimento

        return mais_caro, mais_barato

    def abrir_tela(self):
        self.controlador_sistema.tela_sistema.abrir_tela_atendimento()