import connexion
import six

from swagger_server.models.request_crear_contacto import RequestCrearContacto  # noqa: E501
from swagger_server.models.request_crear_usuario import RequestCrearUsuario  # noqa: E501
from swagger_server.models.response import Response  # noqa: E501
from swagger_server import util


def post_createcontacto(body=None):  # noqa: E501
    """post_createcontacto

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        body = RequestCrearContacto.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_createusuario(body=None):  # noqa: E501
    """post_createusuario

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        body = RequestCrearUsuario.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
