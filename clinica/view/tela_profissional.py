'''
class TelaProfissional:

    def __init__(self, controlador_sistema):
        self.controlador_sistema = controlador_sistema

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
        if len(profissionais) == 0:
            print("Nenhum profissional cadastrado.")
            return
        for i in range(len(profissionais)):
            print(i, "-", profissionais[i].nome, "|", profissionais[i].registro)

    def abrir_tela(self):
        while True:
            print("\nMenu Profissionais")
            print("(1) Incluir profissional")
            print("(2) Listar profissionais")
            print("(3) Alterar profissional")
            print("(4) Excluir profissional")
            print("(5) Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                try:
                    dados = self.obter_dados_profissional()
                    self.controlador_sistema.controlador_profissional.incluir_profissional(
                        dados["especialidade"],
                        dados["registro"],
                        dados["nome"],
                        dados["celular"],
                        dados["cpf"]
                    )
                    print("Profissional cadastrado com sucesso!")
                except ValueError as e:
                    print("Erro:", e)

            elif opcao == "2":
                profissionais = self.controlador_sistema.controlador_profissional.listar_profissionais()
                self.mostrar_profissionais(profissionais)

            elif opcao == "3":
                registro = input("Registro do profissional a alterar: ")
                nova_especialidade = input("Nova especialidade: ")
                novo_nome = input("Novo nome: ")
                novo_celular = input("Novo celular: ")
                try:
                    self.controlador_sistema.controlador_profissional.alterar_profissional(
                        registro, nova_especialidade, novo_nome, novo_celular
                    )
                    print("Profissional alterado com sucesso!")
                except ValueError as e:
                    print("Erro:", e)

            elif opcao == "4":
                registro = input("Registro do profissional a excluir: ")
                try:
                    self.controlador_sistema.controlador_profissional.excluir_profissional(registro)
                    print("Profissional excluído com sucesso!")
                except ValueError as e:
                    print("Erro:", e)

            elif opcao == "5":
                break

            else:
                print("Opção inválida!")
'''