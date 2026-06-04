from model.profissional import Profissional

class ControladorProfissional:

    def __init__(self):
        self.profissionais = []

    def incluir_profissional(
        self,
        especialidade,
        registro,
        nome,
        celular,
        cpf
    ):

        profissional = Profissional(
            especialidade,
            registro,
            nome,
            celular,
            cpf
        )

        self.profissionais.append(profissional)

    def listar_profissionais(self):
        return self.profissionais

    def excluir_profissional(self, registro):
        for profissional in self.profissionais:
            if profissional.registro == registro:
                self.profissionais.remove(profissional)
                break

    def alterar_profissional(
        self,
        registro,
        nova_especialidade,
        novo_nome,
        novo_celular
    ):
        for profissional in self.profissionais:

            if profissional.registro == registro:
                profissional.especialidade = nova_especialidade
                profissional.nome = novo_nome
                profissional.celular = novo_celular
                break
