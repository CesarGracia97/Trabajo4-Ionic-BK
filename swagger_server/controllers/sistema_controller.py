import connexion
import six
from flask import jsonify

from swagger_server.models.request_iniciar_sesion import RequestIniciarSesion  # noqa: E501
from swagger_server.models.request_recuperar_clave import RequestRecuperarClave  # noqa: E501
from swagger_server.models.response import Response  # noqa: E501
from swagger_server import util
from swagger_server.uses_cases.db_queries_methods import DB_Queries_Methods


def iniciar_sesion(body=None):  # noqa: E501
    if connexion.request.is_json:
        body = RequestIniciarSesion.from_dict(connexion.request.get_json())  # noqa: E501
        db = DB_Queries_Methods()
        login =  db.query_iniciar_sesion(body.correo, body.contrasena)
        return jsonify(login), login['status']



def recuperar_contrasena(body=None):  # noqa: E501
    if connexion.request.is_json:
        body = RequestRecuperarClave.from_dict(connexion.request.get_json())  # noqa: E501
        db = DB_Queries_Methods()
        recovery = db.query_recuperar_cuenta(body.correo)
        return jsonify(recovery), recovery['status']
