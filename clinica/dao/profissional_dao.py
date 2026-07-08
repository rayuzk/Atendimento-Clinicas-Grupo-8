from dao.base_dao import BaseDAO


class ProfissionalDAO(BaseDAO):

    def __init__(self):
        super().__init__("profissionais.pkl")
