from dao.base_dao import BaseDAO


class PagamentoDAO(BaseDAO):

    def __init__(self):
        super().__init__("pagamentos.pkl")