from dao.base_dao import BaseDAO


class PacienteDAO(BaseDAO):

    def __init__(self):
        super().__init__("pacientes.pkl")
