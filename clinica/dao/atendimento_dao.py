from dao.base_dao import BaseDAO


class AtendimentoDAO(BaseDAO):

    def __init__(self):
        super().__init__("atendimentos.pkl")