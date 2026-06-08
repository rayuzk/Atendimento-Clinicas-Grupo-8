from model.profissional import Profissional

class ControladorProfissional:

    def __init__(self, controlador_sistema):
        self.controlador_sistema = controlador_sistema
        self.profissionais = []

    def incluir_profissional(self, especialidade, registro, nome, celular, cpf):
        if not nome:
            raise ValueError("Nome não pode ser vazio.")
        if not registro:
            raise ValueError("Registro não pode ser vazio.")
        if not cpf:
            raise ValueError("CPF não pode ser vazio.")

        profissional = Profissional(especialidade, registro, nome, celular, cpf)
        self.profissionais.append(profissional)
        return profissional

    def listar_profissionais(self):
        return self.profissionais

    def excluir_profissional(self, registro):
        for profissional in self.profissionais:
            if profissional.registro == registro:
                self.profissionais.remove(profissional)
                return
        raise ValueError("Profissional não encontrado.")

    def alterar_profissional(self, registro, nova_especialidade, novo_nome, novo_celular):
        for profissional in self.profissionais:
            if profissional.registro == registro:
                profissional.especialidade = nova_especialidade
                profissional.nome = novo_nome
                profissional.celular = novo_celular
                return
        raise ValueError("Profissional não encontrado.")

    def abrir_tela(self):
        self.controlador_sistema.tela_sistema.abrir_tela_profissional()
