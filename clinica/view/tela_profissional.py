class TelaProfissional:

    def obter_dados_profissional(self):

        nome = input("Nome: ")
        celular = input("Celular: ")
        cpf = input("CPF: ")
        especialidade = input("Especialidade: ")
        registro = input("Registro: ")

        return {
            "nome": nome,
            "celular": celular,
            "cpf": cpf,
            "especialidade": especialidade,
            "registro": registro
        }

    def mostrar_profissionais(self, profissionais):

        for profissional in profissionais:
            print(profissional.nome)
