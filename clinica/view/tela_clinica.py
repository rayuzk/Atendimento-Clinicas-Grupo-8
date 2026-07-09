'''
class TelaClinica:

    def __init__(self, controlador_sistema):
        self.controlador_sistema = controlador_sistema

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
        if len(clinicas) == 0:
            print("Nenhuma clínica cadastrada.")
            return
        for i in range(len(clinicas)):
            print(i, "-", clinicas[i].nome, "|", clinicas[i].cidade)

    def abrir_tela(self):
        while True:
            print("\nMenu Clínicas")
            print("(1) Incluir clínica")
            print("(2) Listar clínicas")
            print("(3) Alterar clínica")
            print("(4) Excluir clínica")
            print("(5) Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                dados = self.obter_dados_clinica()
                try:
                    self.controlador_sistema.controlador_clinica.incluir_clinica(
                        dados["nome"],
                        dados["cidade"],
                        dados["descricao"]
                    )
                    print("Clínica cadastrada com sucesso!")
                except ValueError as e:
                    print("Erro:", e)

            elif opcao == "2":
                clinicas = self.controlador_sistema.controlador_clinica.listar_clinicas()
                self.mostrar_clinicas(clinicas)

            elif opcao == "3":
                nome = input("Nome da clínica a alterar: ")
                nova_cidade = input("Nova cidade: ")
                nova_descricao = input("Nova descrição: ")
                try:
                    self.controlador_sistema.controlador_clinica.alterar_clinica(
                        nome, nova_cidade, nova_descricao
                    )
                    print("Clínica alterada com sucesso!")
                except ValueError as e: 
                    print("Erro:", e)

            elif opcao == "4":
                nome = input("Nome da clínica a excluir: ")
                try:
                    self.controlador_sistema.controlador_clinica.excluir_clinica(nome)
                    print("Clínica excluída com sucesso!")
                except ValueError as e:
                    print("Erro:", e)

            elif opcao == "5":
                break

            else:
                print("Opção inválida!")
'''