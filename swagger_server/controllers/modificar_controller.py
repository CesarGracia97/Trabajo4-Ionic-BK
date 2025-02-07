import connexion
import six
from flask import jsonify

from swagger_server.models.request_bloquear_contacto import RequestBloquearContacto  # noqa: E501
from swagger_server.models.request_bloquear_usuario import RequestBloquearUsuario  # noqa: E501
from swagger_server.models.request_modificar_contacto import RequestModificarContacto  # noqa: E501
from swagger_server.models.request_modificar_usuario import RequestModificarUsuario  # noqa: E501
from swagger_server.models.response import Response  # noqa: E501
from swagger_server import util
from swagger_server.uses_cases.db_update_methods import DB_Update_Method
from swagger_server.utils.resource.mysql_configuration import MySQL_Configuration


def put_bloqcontact(body=None):  # noqa: E501
    if connexion.request.is_json:
        body = RequestBloquearContacto.from_dict(connexion.request.get_json())  # noqa: E501
        db = DB_Update_Method()
        put = db.bloquear_contact(body.id)
        return jsonify(put), put['status']


def put_bloqusuario(body=None):  # noqa: E501
    if connexion.request.is_json:
        body = RequestBloquearUsuario.from_dict(connexion.request.get_json())  # noqa: E501
        db = DB_Update_Method()
        put = db.bloquear_usuario(body.id)
        return jsonify(put), put['status']

def put_contacto(body=None):  # noqa: E501
    if connexion.request.is_json:
        body = RequestModificarContacto.from_dict(connexion.request.get_json())  # noqa: E501
        db = DB_Update_Method()
        put = db.update_contact(body.nombre, body.correo, body.telefono, body.id)
        return jsonify(put), put['status']


def put_usuario(body=None):  # noqa: E501
    if connexion.request.is_json:
        body = RequestModificarUsuario.from_dict(connexion.request.get_json())  # noqa: E501
        db = DB_Update_Method()
        put = db.update_usuario(body.contacto, body.nombre, body.id)
        return jsonify(put), put['status']
