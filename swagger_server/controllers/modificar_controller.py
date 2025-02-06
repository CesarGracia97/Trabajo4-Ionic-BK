import connexion
import six

from swagger_server.models.request_bloquear_contacto import RequestBloquearContacto  # noqa: E501
from swagger_server.models.request_bloquear_usuario import RequestBloquearUsuario  # noqa: E501
from swagger_server.models.request_modificar_contacto import RequestModificarContacto  # noqa: E501
from swagger_server.models.request_modificar_usuario import RequestModificarUsuario  # noqa: E501
from swagger_server.models.response import Response  # noqa: E501
from swagger_server import util


def put_bloqcontact(body=None):  # noqa: E501
    """put_bloqcontact

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        body = RequestBloquearContacto.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_bloqusuario(body=None):  # noqa: E501
    """put_bloqusuario

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        body = RequestBloquearUsuario.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_contacto(body=None):  # noqa: E501
    """put_contacto

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        body = RequestModificarContacto.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_usuario(body=None):  # noqa: E501
    """put_usuario

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        body = RequestModificarUsuario.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
