class TelaTipoAtendimento:

    def obter_dados_tipo_atendimento(self):

        descricao = input("Descrição: ")

        return {
            "descricao": descricao
        }

    def mostrar_tipos_atendimento(
        self,
        tipos_atendimento
    ):

        for tipo_atendimento in tipos_atendimento:
            print(tipo_atendimento.descricao)
