import connexion
import six
from flask import jsonify

from swagger_server.models.request_crear_contacto import RequestCrearContacto  # noqa: E501
from swagger_server.models.request_crear_usuario import RequestCrearUsuario  # noqa: E501
from swagger_server.models.response import Response  # noqa: E501
from swagger_server import util
from swagger_server.uses_cases.db_insert_methods import DB_Insert_Methods


def post_createcontacto(body=None):  # noqa: E501
    if connexion.request.is_json:
        body = RequestCrearContacto.from_dict(connexion.request.get_json())  # noqa: E501
        db = DB_Insert_Methods()
        crear = db.create_contacto(body.usuario_id, body.nombre, body.telefono, body.correo, body.cedula)
        return  jsonify(crear), crear['status']


def post_createusuario(body=None):  # noqa: E501
    if connexion.request.is_json:
        body = RequestCrearUsuario.from_dict(connexion.request.get_json())  # noqa: E501
        db = DB_Insert_Methods()
        crear = db.create_usuario(body.correo, body.contrasena, body.nombre, body.cedula, body.contacto)
        return  jsonify(crear), crear['status']
