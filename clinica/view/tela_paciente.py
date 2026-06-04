class TelaPaciente:

    def obter_dados_paciente(self):

        nome = input("Nome: ")
        celular = input("Celular: ")
        cpf = input("CPF: ")
        idade = int(input("Idade: "))

        return {
            "nome": nome,
            "celular": celular,
            "cpf": cpf,
            "idade": idade
        }

    def mostrar_pacientes(self, pacientes):

        for paciente in pacientes:
            print(paciente.nome)
