from model.paciente import Paciente
from dao.paciente_dao import PacienteDAO


class ControladorPaciente:

    def __init__(self, controlador_sistema):
        self.controlador_sistema = controlador_sistema
        self.__paciente_dao = PacienteDAO()
        self.pacientes = self.__paciente_dao.carregar()

    def incluir_paciente(self, idade, nome, celular, cpf):
        if idade < 18:
            raise ValueError("Paciente deve possuir 18 anos ou mais.")
        if not nome:
            raise ValueError("Nome não pode ser vazio.")
        if not cpf:
            raise ValueError("CPF não pode ser vazio.")

        paciente = Paciente(idade, nome, celular, cpf)
        self.pacientes.append(paciente)
        self.__paciente_dao.salvar(self.pacientes)
        return paciente

    def listar_pacientes(self):
        return self.pacientes

    def excluir_paciente(self, cpf):
        for paciente in self.pacientes:
            if paciente.cpf == cpf:
                self.pacientes.remove(paciente)
                self.__paciente_dao.salvar(self.pacientes)
                return
        raise ValueError("Paciente não encontrado.")

    def alterar_paciente(self, cpf, novo_nome, novo_celular, nova_idade):
        for paciente in self.pacientes:
            if paciente.cpf == cpf:
                if nova_idade < 18:
                    raise ValueError("Paciente deve possuir 18 anos ou mais.")
                paciente.nome = novo_nome
                paciente.celular = novo_celular
                paciente.idade = nova_idade
                self.__paciente_dao.salvar(self.pacientes)
                return
        raise ValueError("Paciente não encontrado.")

    def abrir_tela(self):
        self.controlador_sistema.tela_sistema.abrir_tela_paciente()
