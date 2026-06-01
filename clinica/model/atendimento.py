class Atendimento:
    def __init__(
        self,
        clinica,
        paciente,
        profissional,
        data,
        horario_inicio,
        horario_fim,
        tipo_atendimento,
        valor
    ):

        self.clinica = clinica
        self.paciente = paciente
        self.profissional = profissional
        self.data = data
        self.horario_inicio = horario_inicio
        self.horario_fim = horario_fim
        self.tipo_atendimento = tipo_atendimento
        self.valor = valor

        self.procedimentos = []
        self.pagamentos = [] 