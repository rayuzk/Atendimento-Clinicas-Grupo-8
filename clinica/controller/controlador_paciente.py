from model.paciente import Paciente

class ControladorPaciente:

    def __init__(self, controlador_sistema):
        self.controlador_sistema = controlador_sistema
        self.pacientes = []

    def incluir_paciente(self, idade, nome, celular, cpf):
        if idade < 18:
            raise ValueError("Paciente deve possuir 18 anos ou mais.")
        if not nome:
            raise ValueError("Nome não pode ser vazio.")
        if not cpf:
            raise ValueError("CPF não pode ser vazio.")

        paciente = Paciente(idade, nome, celular, cpf)
        self.pacientes.append(paciente)
        return paciente

    def listar_pacientes(self):
        return self.pacientes

    def excluir_paciente(self, cpf):
        for paciente in self.pacientes:
            if paciente.cpf == cpf:
                self.pacientes.remove(paciente)
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
                return
        raise ValueError("Paciente não encontrado.")

    def abrir_tela(self):
        self.controlador_sistema.tela_sistema.abrir_tela_paciente()
