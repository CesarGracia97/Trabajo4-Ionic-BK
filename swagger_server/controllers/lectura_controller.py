import connexion
import six
from flask import jsonify

from swagger_server.models import RequestUsuario
from swagger_server.models.request_lista_contactos import RequestListaContactos  # noqa: E501
from swagger_server.models.request_lista_usuarios import RequestListaUsuarios  # noqa: E501
from swagger_server.models.response import Response  # noqa: E501
from swagger_server import util
from swagger_server.uses_cases.db_queries_methods import DB_Queries_Methods


def get_read_contactos(body=None):  # noqa: E501
    if connexion.request.is_json:
        body = RequestListaContactos.from_dict(connexion.request.get_json())  # noqa: E501
        db = DB_Queries_Methods()
        leer = db.query_lista_contactos(body.id)
        return jsonify(leer), leer['status']


def get_read_usuarios(body=None):  # noqa: E501
    if connexion.request.is_json:
        body = RequestListaUsuarios.from_dict(connexion.request.get_json())  # noqa: E501
        db = DB_Queries_Methods()
        leer = db.query_Lista_usuario()
        return jsonify(leer), leer['status']


def read_user(body=None):  # noqa: E501
    if connexion.request.is_json:
        body = RequestUsuario.from_dict(connexion.request.get_json())  # noqa: E5
        db = DB_Queries_Methods()
        leer = db.query_usuarios(body.id)
        return jsonify(leer), leer['status']
