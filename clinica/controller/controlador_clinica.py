from modelo.clinica import Clinica

class ControladorClinica:

    def __init__(self):
        self.clinicas = []

    def incluir_clinica(self, nome, cidade, descricao):
        clinica = Clinica(nome, cidade, descricao)
        self.clinicas.append(clinica)

    def listar_clinicas(self):
        return self.clinicas

    def excluir_clinica(self, nome):
        for clinica in self.clinicas:
            if clinica.nome == nome:
                self.clinicas.remove(clinica)
                break

    def alterar_clinica(self, nome, nova_cidade, nova_descricao):
        for clinica in self.clinicas:
            if clinica.nome == nome:
                clinica.cidade = nova_cidade
                clinica.descricao = nova_descricao
                break
