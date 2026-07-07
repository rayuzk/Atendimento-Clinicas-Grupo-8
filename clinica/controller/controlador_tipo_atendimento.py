from model.tipo_atendimento import TipoAtendimento
from dao.tipo_atendimento_dao import TipoAtendimentoDAO


class ControladorTipoAtendimento:

    def __init__(self, controlador_sistema):
        self.controlador_sistema = controlador_sistema
        self.__tipo_atendimento_dao = TipoAtendimentoDAO()
        self.tipos_atendimento = self.__tipo_atendimento_dao.carregar()

    def incluir_tipo_atendimento(self, descricao):
        if not descricao:
            raise ValueError("Descrição não pode ser vazia.")

        tipo_atendimento = TipoAtendimento(descricao)
        self.tipos_atendimento.append(tipo_atendimento)
        self.__tipo_atendimento_dao.salvar(self.tipos_atendimento)
        return tipo_atendimento

    def listar_tipos_atendimento(self):
        return self.tipos_atendimento

    def excluir_tipo_atendimento(self, descricao):
        for tipo_atendimento in self.tipos_atendimento:
            if tipo_atendimento.descricao == descricao:
                self.tipos_atendimento.remove(tipo_atendimento)
                self.__tipo_atendimento_dao.salvar(self.tipos_atendimento)
                return
        raise ValueError("Tipo de atendimento não encontrado.")

    def alterar_tipo_atendimento(self, descricao, nova_descricao):
        for tipo_atendimento in self.tipos_atendimento:
            if tipo_atendimento.descricao == descricao:
                tipo_atendimento.descricao = nova_descricao
                self.__tipo_atendimento_dao.salvar(self.tipos_atendimento)
                return
        raise ValueError("Tipo de atendimento não encontrado.")

    def abrir_tela(self):
        self.controlador_sistema.tela_sistema.abrir_tela_tipo_atendimento()
