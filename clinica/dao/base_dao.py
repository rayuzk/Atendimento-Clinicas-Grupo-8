import os
import pickle


class BaseDAO:

    def __init__(self, nome_arquivo):
        self.__nome_arquivo = nome_arquivo

    def carregar(self):
        if not os.path.exists(self.__nome_arquivo):
            return []

        with open(self.__nome_arquivo, "rb") as arquivo:
            return pickle.load(arquivo)

    def salvar(self, dados):
        with open(self.__nome_arquivo, "wb") as arquivo:
            pickle.dump(dados, arquivo)
