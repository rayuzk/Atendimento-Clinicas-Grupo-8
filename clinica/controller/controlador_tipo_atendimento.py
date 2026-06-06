from model.tipo_atendimento import TipoAtendimento

class ControladorTipoAtendimento:

    def __init__(self):
        self.tipos_atendimento = []

    def incluir_tipo_atendimento(self, descricao):

        tipo_atendimento = TipoAtendimento(descricao)

        self.tipos_atendimento.append(tipo_atendimento)

    def listar_tipos_atendimento(self):
        return self.tipos_atendimento

    def excluir_tipo_atendimento(self, descricao):

        for tipo_atendimento in self.tipos_atendimento:

            if tipo_atendimento.descricao == descricao:
                self.tipos_atendimento.remove(tipo_atendimento)
                break

    def alterar_tipo_atendimento(
        self,
        descricao,
        nova_descricao
    ):

        for tipo_atendimento in self.tipos_atendimento:

            if tipo_atendimento.descricao == descricao:
                tipo_atendimento.descricao = nova_descricao
                break

    def abrir_tela(self):
        pass
