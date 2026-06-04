class TelaClinica:

    def obter_dados_clinica(self):

        nome = input("Nome: ")
        cidade = input("Cidade: ")
        descricao = input("Descrição: ")

        return {
            "nome": nome,
            "cidade": cidade,
            "descricao": descricao
        }

    def mostrar_clinicas(self, clinicas):

        for clinica in clinicas:
            print(clinica.nome)
