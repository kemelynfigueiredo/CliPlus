from app.repository.pacientes_repository import buscar_por_cpf

from app.repository.pacientes_repository import listar_todos

def buscar_paciente_por_cpf(cpf: str):
    paciente = buscar_por_cpf(cpf)
    return paciente


def listar_pacientes(limit: int = 100):
    return listar_todos(limit)