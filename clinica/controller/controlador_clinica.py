from model.clinica import Clinica
from dao.clinica_dao import ClinicaDAO


class ControladorClinica:

    def __init__(self, controlador_sistema):
        self.controlador_sistema = controlador_sistema
        self.__clinica_dao = ClinicaDAO()
        self.clinicas = self.__clinica_dao.carregar()

    def incluir_clinica(self, nome, cidade, descricao):
        if not nome:
            raise ValueError("Nome da clínica não pode ser vazio.")
        if not cidade:
            raise ValueError("Cidade não pode ser vazia.")

        clinica = Clinica(nome, cidade, descricao)
        self.clinicas.append(clinica)
        self.__clinica_dao.salvar(self.clinicas)
        return clinica

    def listar_clinicas(self):
        return self.clinicas

    def excluir_clinica(self, nome):
        for clinica in self.clinicas:
            if clinica.nome == nome:
                self.clinicas.remove(clinica)
                self.__clinica_dao.salvar(self.clinicas)
                return
        raise ValueError("Clínica não encontrada.")

    def alterar_clinica(self, nome, nova_cidade, nova_descricao):
        for clinica in self.clinicas:
            if clinica.nome == nome:
                clinica.cidade = nova_cidade
                clinica.descricao = nova_descricao
                self.__clinica_dao.salvar(self.clinicas)
                return
        raise ValueError("Clínica não encontrada.")

    def abrir_tela(self):
        self.controlador_sistema.tela_sistema.abrir_tela_clinica()
