import re
from flask import jsonify
from apiflask import APIBlueprint
from app.services.pacientes_service import buscar_paciente_por_cpf, listar_pacientes
from app.helpers.auth import auth
from app.schemas.paciente_schema import PacienteSchema

bp = APIBlueprint("pacientes", __name__)

@bp.get("/pacientes/<string:cpf>")
@bp.auth_required(auth)

def get_paciente_por_cpf(cpf):
    cpf_limpo = re.sub(r"\D", "", cpf)
    if len(cpf_limpo) != 11:
        return jsonify({"erro": "CPF inválido"}), 400

    paciente = buscar_paciente_por_cpf(cpf_limpo)

    if not paciente:
        return jsonify({"erro": "Paciente não encontrado"}), 404

    return jsonify(paciente), 200


@bp.get("/pacientes")
@bp.auth_required(auth)
def get_pacientes():
    # opcional: permitir query param ?limit=xx
    from flask import request
    try:
        limit = int(request.args.get("limit", 100))
    except ValueError:
        limit = 100

    pacientes = listar_pacientes(limit=limit)
    return jsonify(pacientes), 200