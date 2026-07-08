from dao.base_dao import BaseDAO


class ClinicaDAO(BaseDAO):

    def __init__(self):
        super().__init__("clinicas.pkl")
